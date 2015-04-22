from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
from Colin.PFSim.particles.tlv.jet import Jet

from ROOT import heppy 

import math
    
class JetClusterizer(Analyzer):

    def beginLoop(self, setup):
        super(JetClusterizer, self).beginLoop(setup)
        self.clusterizer = heppy.JetClusterizer()
      
    def process(self, event):
        particles = getattr(event, self.cfg_ana.particles)
        self.clusterizer.clear();
        for ptc in particles:
            self.clusterizer.add_p4( ptc.p4() )
        self.clusterizer.clusterize()
        self.mainLogger.info( 'njets = {n}'.format(
            n=self.clusterizer.n_jets()))
        jets = []
        for jeti in range(self.clusterizer.n_jets()):
            jet = Jet( self.clusterizer.jet(jeti) )
            jets.append( jet )
            self.mainLogger.info( '\t{jet}'.format(jet=jet))
        setattr(event, '_'.join([self.instance_label,'jets']), jets)

