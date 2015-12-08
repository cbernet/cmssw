

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle

from Colin.Met.analyzers.MET import METSimple


class RecoMetReader( Analyzer ):

    def declareHandles(self):
        super(RecoMetReader, self).declareHandles()       
        self.type, self.colname = self.cfg_ana.met
        self.handles['met'] =  AutoHandle(
            self.colname, self.type
            )
        

    def beginLoop(self, setup):
        super(RecoMetReader,self).beginLoop(setup)

       
    def process(self, event):
        self.readCollections( event.input )
        met = self.handles['met'].product()[0]
        metsimple = METSimple(
            met.pt(), met.px(), met.py(), met.phi(), met.sumEt(), self.colname
            )
        print metsimple
        setattr(event, self.colname, metsimple)



