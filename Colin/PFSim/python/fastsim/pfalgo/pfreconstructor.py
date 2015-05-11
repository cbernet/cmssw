from Colin.PFSim.fastsim.pdt import particle_data
from Colin.PFSim.fastsim.path import StraightLine, Helix
from Colin.PFSim.fastsim.pfobjects import Particle

from ROOT import TVector3, TLorentzVector
import math
import pprint

class PFReconstructor(object):

    def __init__(self, links, detector, logger):
        self.links = links
        self.detector = detector
        self.log = logger
        self.reconstruct(links)

    def reconstruct(self, links):
        self.unused = []
        self.particles = []
        all_subgroups = dict()
        # pprint.pprint( links.groups )
        # import pdb; pdb.set_trace()
        for groupid, group in links.groups.iteritems():
            if self.simplify_group(group):
                all_subgroups[groupid] = links.subgroups(groupid)
        for group_id, subgroups in all_subgroups.iteritems():
            del links.groups[group_id]
            links.groups.update(subgroups)
        for group_id, group in links.groups.iteritems():
            self.log.info( "group {group_id} {group}".format(
                group_id = group_id,
                group = group) ) 
            self.particles.extend( self.reconstruct_group(group) )
        self.unused = [elem for elem in links.elements if not elem.locked]
        self.log.info("Particles:")
        self.log.info(str(self))
            
    def simplify_group(self, group):
        # for each track, keeping only the closest hcal link
        simplified = False
        assert(len(group)!=0)
        if len(group)==1:
            return False
        tracks = [elem for elem in group if elem.layer=='tracker']
        for track in tracks:
            first_hcal = True
            to_unlink = []
            for linked in track.linked:
                if linked.layer == 'hcal_in':
                    if first_hcal:
                        first_hcal = False
                    else:
                        to_unlink.append(linked)
            for linked in to_unlink:
                self.links.unlink(track, linked)
                simplified = True
        # remove all ecal-hcal links. ecal linked to hcal give rise to a photon anyway.
        ecals = [elem for elem in group if elem.layer=='ecal_in']
        for ecal in ecals:
            to_unlink = []
            for linked in ecal.linked:
                if linked.layer == 'hcal_in':
                    to_unlink.append(linked)
            for linked in to_unlink:
                self.links.unlink(ecal, linked)
                simplified = True
        return simplified
            
    def reconstruct_group(self, group):
        particles = []
        if len(group)==1: #TODO WARNING!!! LOTS OF MISSING CASES
            elem = group[0]
            layer = elem.layer
            if layer == 'ecal_in' or layer == 'hcal_in':
                particles.append(self.reconstruct_cluster(elem, layer))
            elif layer == 'tracker':
                particles.append(self.reconstruct_track(elem))
            elem.locked = True
        else:
            hcals = [elem for elem in group if elem.layer=='hcal_in']
            for hcal in hcals:
                particles.extend(self.reconstruct_hcal(hcal))
            #TODO deal with ecal-ecal
            ecals = [elem for elem in group if elem.layer=='ecal_in'
                     and not elem.locked]
            for ecal in ecals:
                linked_layers = [linked.layer for linked in ecal.linked]
                # assert('tracker' not in linked_layers) #TODO electrons
                self.log.warning( 'DEAL WITH ELECTRONS!' ) 
                particles.append(self.reconstruct_cluster(ecal, 'ecal_in'))
            #TODO deal with track-ecal
        return particles 

    def reconstruct_hcal(self, hcal):
        particles = []
        tracks = []
        ecals = []
        for elem in hcal.linked:
            assert(elem.layer!='ecal_in') # should have killed ecal-hcal links
            if elem.layer == 'hcal_in':
                continue
            elif elem.layer == 'tracker':
                tracks.append(elem)
                for ecal in elem.linked:
                    if ecal.layer!='ecal_in':
                        continue
                    ecals.append(ecal)
                    ecal.locked = True
                # ecals.extend([te for te in elem.linked if te.layer=='ecal_in'])
                # hcal should be the only remaining linked hcal cluster (closest one)
                thcals = [th for th in elem.linked if th.layer=='hcal_in']
                assert(thcals[0]==hcal)
        self.log.info( hcal )
        self.log.info( '\tT {tracks}'.format(tracks=tracks) )
        self.log.info( '\tE {ecals}'.format(ecals=ecals) )
        hcal_energy = hcal.energy
        if len(tracks):
            ecal_energy = sum(ecal.energy for ecal in ecals)
            track_energy = sum(track.energy for track in tracks)
            for track in tracks:
                particles.append(self.reconstruct_track(track))
            delta_e_rel = (hcal_energy + ecal_energy) / track_energy - 1.
            calo_eres = self.detector.elements['hcal'].energy_resolution(track_energy)
            self.log.info( 'dE/p, res = {derel}, {res} '.format(
                derel = delta_e_rel,
                res = calo_eres ))
            if delta_e_rel > calo_eres:
                excess = delta_e_rel * track_energy
                self.log.info( 'excess = {excess:5.2f}, ecal_E = {ecal_e:5.2f}, diff = {diff:5.2f}'.format(
                    excess=excess, ecal_e = ecal_energy, diff=excess-ecal_energy)) 
                if excess <= ecal_energy:
                    particles.append(self.reconstruct_cluster(hcal, 'ecal_in',
                                                              excess))
                else:
                    particle = self.reconstruct_cluster(hcal, 'hcal_in',
                                                        excess-ecal_energy)
                    if particle:
                        particles.append(particle)
                    if ecal_energy:
                        particles.append(self.reconstruct_cluster(hcal, 'ecal_in',
                                                                  ecal_energy))

        else:
            # hcal cluster linked to other hcal clusters 
            for elem in hcal.linked:
                assert(elem.layer=='hcal_in')
                # ecal hcal links have been cut
            particles.append(self.reconstruct_cluster(hcal, 'hcal_in'))
           
        return particles 
                
    def reconstruct_cluster(self, cluster, layer, energy=None, vertex=None):
        if vertex is None:
            vertex = TVector3()
        pdg_id = None
        if layer=='ecal_in':
            pdg_id = 22
        elif layer=='hcal_in':
            pdg_id = 130
        else:
            raise ValueError('layer must be equal to ecal_in or hcal_in')
        assert(pdg_id)
        mass, charge = particle_data[pdg_id]
        if energy is None:
            energy = cluster.energy
        if energy < mass: 
            return None 
        momentum = math.sqrt(energy**2 - mass**2)
        p3 = cluster.position.Unit() * momentum
        p4 = TLorentzVector(p3.Px(), p3.Py(), p3.Pz(), energy)
        particle = Particle(p4, vertex, charge, pdg_id)
        path = StraightLine(p4, vertex)
        path.points[layer] = cluster.position
        particle.set_path(path)
        particle.clusters_smeared[layer] = cluster
        cluster.locked = True
        return particle
        
    def reconstruct_track(self, track):
        vertex = track.path.points['vertex']
        pdg_id = 211 * track.charge
        try: 
            mass, charge = particle_data[pdg_id]
        except KeyError:
            import pdb; pdb.set_trace()
        p4 = TLorentzVector()
        p4.SetVectM(track.p3, mass)
        particle = Particle(p4, vertex, charge, pdg_id)
        particle.set_path(track.path)
        track.locked = True
        return particle


    def __str__(self):
        theStr = ['Particles:']
        theStr.extend( map(str, self.particles))
        theStr.append('Unused:')
        if len(self.unused)==0:
            theStr.append('None')
        else:
            theStr.extend( map(str, self.unused))
        return '\n'.join( theStr )
