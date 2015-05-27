from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from Colin.PFSim.particles.fcc.particle import Particle 

import math

class FCCReader(Analyzer):
    
    def process(self, event):
        store = event.input
        gen_particles = map(Particle, store.get("GenParticle"))
        event.gen_particles = sorted( gen_particles,
                                      key = lambda ptc: ptc.e(), reverse=True )  
        event.gen_particles_stable = [ptc for ptc in event.gen_particles
                                      if ptc.status()==1 and not math.isnan(ptc.e())]

        
