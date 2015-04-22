from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from Colin.PFSim.particles.fcc.particle import Particle 

import math
from Colin.PFSim.fastsim.detectors.CMS import CMS
from Colin.PFSim.fastsim.simulator import Simulator
from Colin.PFSim.fastsim.vectors import Point
from Colin.PFSim.fastsim.pfobjects import Particle as PFSimParticle
from Colin.PFSim.fastsim.toyevents import particles
from Colin.PFSim.display.core import Display
from Colin.PFSim.display.geometry import GDetector
from Colin.PFSim.display.pfobjects import GTrajectories

from ROOT import TLorentzVector, TVector3

def pfsimparticle(ptc):
    tp4 = ptc.p4()
    vertex = TVector3()
    charge = ptc.q()
    pid = ptc.pdgid()
    return PFSimParticle(tp4, vertex, charge, pid) 
        
class PFSim(Analyzer):

    def __init__(self, *args, **kwargs):
        super(PFSim, self).__init__(*args, **kwargs)
        self.detector = CMS()
        self.simulator = Simulator(self.detector, self.mainLogger)
        self.is_display = self.cfg_ana.display
        if self.is_display:
            self.init_display()        
        
    def init_display(self):
        self.display = Display(['xy','yz', 'ECAL_thetaphi', 'HCAL_thetaphi'])
        self.gdetector = GDetector(self.detector)
        self.display.register(self.gdetector, layer=0, clearable=False)
        self.is_display = True
        
    def process(self, event):
        if self.is_display:
            self.display.clear()
        pfsim_particles = []
        for ptc in event.gen_particles_stable:
            if not math.isnan(ptc.pt()) and ptc.pt()>1.:
                pfsimptc = pfsimparticle(ptc)
                pfsim_particles.append(pfsimptc)
                if self.cfg_ana.verbose:
                    print pyptc
        self.simulator.simulate( pfsim_particles )
        if self.is_display:
            self.display.register( GTrajectories(pfsim_particles), layer=1)        
        event.simparticles = sorted( pfsim_particles,
                                     key = lambda ptc: ptc.e(), reverse=True)
        event.particles = sorted( self.simulator.pfsequence.pfreco.particles,
                                  key = lambda ptc: ptc.e(), reverse=True)

