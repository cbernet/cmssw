
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject as Tau


class TauAnalyzer( Analyzer ):

    def declareHandles(self):
        super(TauAnalyzer, self).declareHandles()
        if 'PFTau' in self.cfg_ana.taus:
            self.handles['taus'] =  AutoHandle(
                self.cfg_ana.taus, 'std::vector<reco::PFTau>'
                )
            self.handles['discs'] =  AutoHandle(
                self.cfg_ana.discs, 'reco::PFTauDiscriminator'
                )


    def beginLoop(self, setup):
        super(TauAnalyzer,self).beginLoop(setup)

       
    def process(self, event):
        self.readCollections( event.input )
        discs = self.handles['discs'].product()
        print event.iEv
        for itau, htau in  enumerate(self.handles['taus'].product()):
            tau = Tau(htau)
            tau.disc = discs[itau].second
            print tau.pt(), tau.disc
        
        




