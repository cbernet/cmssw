from Colin.PFSim.fastsim.propagator import StraightLinePropagator, HelixPropagator
from Colin.PFSim.fastsim.pfobjects import Cluster, SmearedCluster, SmearedTrack
from pfalgo.sequence import PFSequence
import random
import sys


class Simulator(object):

    def __init__(self, detector, logger=None):
        self.verbose = True
        self.detector = detector
        if logger is None:
            import logging
            logging.basicConfig(level='ERROR')
            logger = logging.getLogger('Simulator')
        self.logger = logger
        self.prop_helix = HelixPropagator()
        self.prop_straight = StraightLinePropagator()
        
    def reset(self):
        self.particles = None
        Cluster.max_energy = 0.
        SmearedCluster.max_energy = 0.
        
    def propagator(self, ptc):
        is_neutral = abs(ptc.q())<0.5
        return self.prop_straight if is_neutral else self.prop_helix
        
    def propagate(self, ptc):
        '''propagate the particle to all detector cylinders'''
        self.propagator(ptc).propagate([ptc], self.detector.cylinders(),
                                       self.detector.elements['field'].magnitude)

    def make_cluster(self, ptc, detname, fraction=1., size=None):
        '''adds a cluster in a given detector, with a given fraction of 
        the particle energy.'''
        detector = self.detector.elements[detname]
        self.propagator(ptc).propagate_one(ptc,
                                           detector.volume.inner,
                                           self.detector.elements['field'].magnitude )
        if size is None:
            size = detector.cluster_size(ptc)
        cylname = detector.volume.inner.name
        cluster =  Cluster(ptc.p4().E()*fraction,
                           ptc.points[cylname],
                           size,
                           cylname, ptc)
        ptc.clusters[cylname] = cluster
        return cluster

    def smear_cluster(self, cluster, detector, accept=False):
        '''Returns a copy of self with a smeared energy.  
        If accept is False (default), returns None if the smeared 
        cluster is not in the detector acceptance. '''
        eres = detector.energy_resolution(cluster.energy)
        energy = cluster.energy * random.gauss(1, eres)
        smeared_cluster = SmearedCluster( cluster,
                                          energy,
                                          cluster.position,
                                          cluster.size(),
                                          cluster.layer,
                                          cluster.particle )
        # smeared_cluster.set_energy(energy)
        if detector.acceptance(smeared_cluster) or accept:
            return smeared_cluster
        else:
            return None
    
    def smear_track(self, track, detector, accept=False):
        #TODO smearing depends on particle type!
        ptres = detector.pt_resolution(track)
        scale_factor = random.gauss(1, ptres)
        smeared_track = SmearedTrack(track,
                                     track.p3 * scale_factor,
                                     track.charge,
                                     track.path)
        if detector.acceptance(smeared_track) or accept:
            return smeared_track
        else:
            return None
        
    def simulate_photon(self, ptc):
        detname = 'ecal'
        ecal = self.detector.elements[detname]
        self.prop_straight.propagate_one(ptc,
                                         ecal.volume.inner)
        
        cluster = self.make_cluster(ptc, detname)
        smeared = self.smear_cluster(cluster, ecal)
        if smeared: 
            ptc.clusters_smeared[smeared.layer] = smeared


    def simulate_electron(self, ptc):
        ecal = self.detector.elements['ecal']
        self.prop_helix.propagate_one(ptc,
                                      ecal.volume.inner,
                                      self.detector.elements['field'].magnitude )
        cluster = self.make_cluster(ptc, 'ecal')
        smeared_cluster = self.smear_cluster(cluster, ecal)
        if smeared_cluster: 
            ptc.clusters_smeared[smeared_cluster.layer] = smeared_cluster
        smeared_track = self.smear_track(ptc.track,
                                         self.detector.elements['tracker'])
        if smeared_track:
            ptc.track_smeared = smeared_track


    def simulate_neutrino(self, ptc):
        self.propagate(ptc)
        
    def simulate_hadron(self, ptc):
        ecal = self.detector.elements['ecal']
        hcal = self.detector.elements['hcal']        
        frac_ecal = 0.
        self.propagator(ptc).propagate_one(ptc,
                                           ecal.volume.inner,
                                           self.detector.elements['field'].magnitude)
        path_length = ecal.material.path_length(ptc)
        if path_length<sys.float_info.max:
            # ecal path length can be infinite in case the ecal
            # has lambda_I = 0 (fully transparent to hadrons)
            time_ecal_inner = ptc.path.time_at_z(ptc.points['ecal_in'].Z())
            deltat = ptc.path.deltat(path_length)
            time_decay = time_ecal_inner + deltat
            point_decay = ptc.path.point_at_time(time_decay)
            ptc.points['ecal_decay'] = point_decay
            if ecal.volume.contains(point_decay):
                frac_ecal = random.uniform(0., 0.7)
                cluster = self.make_cluster(ptc, 'ecal', frac_ecal)
                # For now, using the hcal resolution and acceptance
                # for hadronic cluster
                # in the ECAL. That's not a bug! 
                smeared = self.smear_cluster(cluster, hcal)
                if smeared:
                    ptc.clusters_smeared[smeared.layer] = smeared
        cluster = self.make_cluster(ptc, 'hcal', 1-frac_ecal)
        smeared = self.smear_cluster(cluster, hcal)
        if smeared:
            ptc.clusters_smeared[smeared.layer] = smeared
        if ptc.q()!=0:
            smeared_track = self.smear_track(ptc.track,
                                             self.detector.elements['tracker'])
            if smeared_track:
                ptc.track_smeared = smeared_track

    def simulate_muon(self, ptc):
        self.propagate(ptc)
        smeared_track = self.smear_track(ptc.track,
                                         self.detector.elements['tracker'])
        if smeared_track:
            ptc.track_smeared = smeared_track
            
    def simulate(self, ptcs):
        self.reset()
        self.ptcs = ptcs
        for ptc in ptcs:
            if ptc.pdgid() == 22:
                self.simulate_photon(ptc)
            elif abs(ptc.pdgid()) == 11:
                self.simulate_electron(ptc)
            elif abs(ptc.pdgid()) == 13:
                self.simulate_muon(ptc)
            elif abs(ptc.pdgid()) in [12,14,16]:
                self.simulate_neutrino(ptc)
            elif abs(ptc.pdgid()) > 100: #TODO make sure this is ok
                self.simulate_hadron(ptc)
        self.pfsequence = PFSequence(self.ptcs, self.detector, self.logger)
        
if __name__ == '__main__':

    import math
    import logging
    from vectors import Point
    from detectors.CMS import cms
    from detectors.perfect import perfect    
    from toyevents import monojet, particle 
    from Colin.PFSim.display.core import Display
    from Colin.PFSim.display.geometry import GDetector
    from Colin.PFSim.display.pfobjects import GTrajectories

    display_on = True
    detector = cms

    logging.basicConfig(level='ERROR')
    logger = logging.getLogger('Simulator')
    logger.addHandler( logging.StreamHandler(sys.stdout) )
    
    for i in range(1):
        if not i%100:
            print i
        simulator = Simulator(detector, logger)
        # particles = monojet([211, -211, 130, 22, 22, 22], math.pi/2., math.pi/2., 2, 50)
        particles = [
            particle(211, math.pi/2., math.pi/2., 100),
            # particle(22, math.pi/2.+0.4, 0., 200.),
            particle(130, math.pi/2., math.pi/2.+0., 100.),
            particle(22, math.pi/2., math.pi/2.+0.0, 50.)
        ]
        simulator.simulate(particles)
        
    if display_on:
        display = Display(['xy', 'yz',
                           'ECAL_thetaphi',
                           'HCAL_thetaphi'
                       ])
        gdetector = GDetector(detector)
        display.register(gdetector, 0)
        gtrajectories = GTrajectories(particles)
        display.register(gtrajectories,1)
        display.draw()
    
