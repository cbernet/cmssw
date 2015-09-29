
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject

class Tau(PhysicsObject):

    def __init__(self, physobj):
        super(Tau, self).__init__(physobj)
        self._isolation = -1
        
    def signalCharged(self):
        '''number of charged tracks in the calo tau signal cone, or of charged 
        PFCandidates in the PFTau'''
        if not hasattr(self, 'leadPFCand'):
            return self.signalTracks()
        else:
            return self.signalPFChargedHadrCands()

    def isolation(self):
        return self._isolation


    def discstr(self, tab):
        strs = []
        for dname, value in self.discs.iteritems():
            strs.append( '{tab}{dname:20} : {value}'.format(tab=tab, 
                                                            dname=dname,
                                                            value=value) )
        return '\n'.join(sorted(strs)) 



class TauAnalyzer( Analyzer ):

    def declareHandles(self):
        super(TauAnalyzer, self).declareHandles()
        self.is_pf = False
        if 'PFTau' in self.cfg_ana.taus:
            self.is_pf = True
            self.handles['taus'] =  AutoHandle(
                self.cfg_ana.taus, 'std::vector<reco::PFTau>'
                )
            for disc in  self.cfg_ana.discs:
                self.handles[disc] =  AutoHandle(
                    disc, 'reco::PFTauDiscriminator'
                    )
        else:
            self.handles['taus'] =  AutoHandle(
                self.cfg_ana.taus, 'std::vector<reco::CaloTau>'
                )
            for disc in  self.cfg_ana.discs:
                self.handles[disc] =  AutoHandle(
                    disc, 'reco::CaloTauDiscriminator'
                    )

    def beginLoop(self, setup):
        super(TauAnalyzer,self).beginLoop(setup)

       
    def process(self, event):
        self.readCollections( event.input )
        all_discs = dict()
        for discname in self.cfg_ana.discs:
            all_discs[discname] = self.handles[discname].product()
        taus = []
        if self.cfg_ana.verbose:
            print event.iEv, '-'*50
        for itau, htau in  enumerate(self.handles['taus'].product()):
            tau = Tau(htau)
            if not self.cfg_ana.select_kin(tau): 
                continue
            tau.discs = dict()
            for discname, disc in all_discs.iteritems():
                value = disc.value(itau)
                tau.discs[discname] = value 
            if self.is_pf:
                charged = tau.discs['hpsPFTauMVA3IsolationChargedIsoPtSum']
                neutral = tau.discs['hpsPFTauMVA3IsolationNeutralIsoPtSum']
                iso = charged + max(0., neutral-2.)
                tau._isolation = iso
            else:
                tau._isolation = -1
            if self.cfg_ana.verbose:
                print tau
                print tau.discstr('\t')
            taus.append(tau)
#            print len(tau.signalCharged())
        setattr(event, 'taudiscs_{label}'.format(label=self.instance_label), self.cfg_ana.discs)
        setattr(event, 'taus_{label}'.format(label=self.instance_label), taus)
#        if len(taus):
#            import pdb; pdb.set_trace()
            
#        print tau.pt(), tau.discs['hpsPFTauDiscriminationByDecayModeFinding'], tau.discs['hpsPFTauDiscriminationByMediumIsolation']
        




