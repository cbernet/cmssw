

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject as PFCandidate
from Colin.MetScanning.analyzers.MET import METBuilder

class PFMetAnalyzer( Analyzer ):

    def declareHandles(self):
        super(PFMetAnalyzer, self).declareHandles()
        self.handles['pfmet'] =  AutoHandle(
            'pfMet', 'std::vector<reco::PFMET>'
            )
        self.cleaned_pf_names = [
            'CleanedCosmicsMuons',
            'CleanedFakeMuons',
            'CleanedHF',
            'CleanedPunchThroughMuons',
            'CleanedPunchThroughNeutralHadrons',
            'CleanedTrackerAndGlobalMuons',
            'CleanedTrackerAndGlobalMuons',
            'AddedMuonsAndHadrons', 
            ]
        def init_cleaned_pf(label):
            self.handles[label] = AutoHandle(
                ':'.join(['particleFlowTmp',label]), 'std::vector<reco::PFCandidate>'
                )
        self.handles['pf'] = AutoHandle(
            'particleFlow', 'std::vector<reco::PFCandidate>'
            )
        map(init_cleaned_pf, self.cleaned_pf_names)
        

    def beginLoop(self, setup):
        super(PFMetAnalyzer,self).beginLoop(setup)

       
    def process(self, event):
        self.readCollections( event.input )
        event.pfmet = self.handles['pfmet'].product()[0]
        # print 'PFMET', event.met.pt(), event.met.phi(), event.met.sumEt()
        #         event.CleanedTrackerAndGlobalMuons = self.handles['CleanedTrackerAndGlobalMuons'].product()
        #     print len(event.CleanedTrackerAndGlobalMuons)
        # for name in self.cleaned_pf_names:
        #    coll = map(PFCandidate, self.handles[name].product())
        #    # print name, len(coll)
        #    setattr(event, name, coll)

        # event.pfcands = map(PFCandidate, self.handles['pf'].product())
        # print 'pf', len(event.pf)
        # event.rec_pfmet = METBuilder(event.pf, 'particleFlow')
        # print event.rec_pfmet
        # print 'diff', event.rec_pfmet.pt() - event.met.pt()
        # print event.pfmet.pt(), event.pfmet.phi()
