

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject as PFCandidate
from Colin.MetScanning.analyzers.MET import METSimple


class MiniAODReader( Analyzer ):

    def declareHandles(self):
        super(MiniAODReader, self).declareHandles()
        if self.cfg_ana.read_pfcands: 
            self.handles['pfcands'] =  AutoHandle(
                'packedPFCandidates', 'std::vector<pat::PackedCandidate>'
                )
        self.handles['mets'] =  AutoHandle(
            'slimmedMETs', 'std::vector<pat::MET>'
            )

        

    def beginLoop(self, setup):
        super(MiniAODReader,self).beginLoop(setup)

       
    def process(self, event):
        self.readCollections( event.input )
        if self.cfg_ana.read_pfcands: 
            event.pfcands = map(PFCandidate, self.handles['pfcands'].product())
        met = self.handles['mets'].product()[0]
        event.maod_met = met 




