
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
            for disc in  self.cfg_ana.discs:
                self.handles[disc] =  AutoHandle(
                    disc, 'reco::PFTauDiscriminator'
                    )

    def beginLoop(self, setup):
        super(TauAnalyzer,self).beginLoop(setup)

       
    def process(self, event):
        self.readCollections( event.input )
        all_discs = dict()
        for discname in self.cfg_ana.discs:
            all_discs[discname] = self.handles[discname].product()
        taus = []
        for itau, htau in  enumerate(self.handles['taus'].product()):
            tau = Tau(htau)
            taus.append(tau)
            if not self.cfg_ana.select_kin(tau): 
                continue
            tau.discs = dict()
            for discname, disc in all_discs.iteritems():
                value = disc[itau].second
                tau.discs[discname] = value
        setattr(event, 'taus_{label}'.format(label=self.instance_label), taus)

#             print tau.pt(), tau.discs['hpsPFTauDiscriminationByDecayModeFinding'], tau.discs['hpsPFTauDiscriminationByMediumIsolation']
        




