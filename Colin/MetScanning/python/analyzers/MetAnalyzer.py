

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from Colin.MetScanning.analyzers.MET import METBuilder, METSimple


class MetAnalyzer( Analyzer ):

    def declareHandles(self):
        super(MetAnalyzer, self).declareHandles()
        

    def beginLoop(self, setup):
        super(MetAnalyzer,self).beginLoop(setup)

       
    def process(self, event):
        pfcands = event.pfcands
        event.pfmet = METBuilder(pfcands, 'pf_all')
        event.pfmet_maod_uncorr = METSimple(event.maod_met.uncorrectedPt(), 
                                            event.maod_met.uncorrectedPhi(), 
                                            event.maod_met.uncorrectedSumEt(), 
                                            'pfmet_maod_uncorr')
    
