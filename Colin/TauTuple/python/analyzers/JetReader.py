from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from Colin.TauTuple.particles.cms.jet import Jet

import math

class JetReader(Analyzer):
    
    def declareHandles(self):
        super(JetReader, self).declareHandles()
        self.handles['jets'] = AutoHandle(
            *self.cfg_ana.jets
            )

    def process(self, event):
        self.readCollections(event.input)
        store = event.input
        genj = self.handles['jets'].product()
        genj = [jet for jet in genj if jet.pt()>self.cfg_ana.jet_pt]
        jets = map(Jet, genj)
        jets = sorted( jets,
                           key = lambda ptc: ptc.pt(), reverse=True ) 
        setattr(event, self.instance_label, jets)
        
        for jet in jets:
            jet.constituents.validate(jet.e())

