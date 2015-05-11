from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from Colin.PFSim.particles.cms.particle import Particle 

import math

class CMSReader(Analyzer):
    
    def declareHandles(self):
        super(CMSReader, self).declareHandles()
        self.handles['gen_particles'] = AutoHandle(
            self.cfg_ana.gen_particles, 
            'std::vector<reco::GenParticle>'
            )
        self.handles['pf_particles'] = AutoHandle(
            self.cfg_ana.pf_particles, 
            'std::vector<reco::PFCandidate>'
            )

    def process(self, event):
        self.readCollections(event.input)
        store = event.input
        genp = self.handles['gen_particles'].product()
        gen_particles = map(Particle, genp)
        event.gen_particles = sorted( gen_particles,
                                      key = lambda ptc: ptc.e(), reverse=True )  
        event.gen_particles_stable = [ptc for ptc in event.gen_particles
                                      if ptc.status()==1 and not math.isnan(ptc.e())]
        pfp = self.handles['pf_particles'].product()
        event.pf_particles = map(Particle, pfp)
        
