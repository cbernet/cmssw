
import copy
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle


class PFMetAnalyzer( Analyzer ):

    def declareHandles(self):
        super(PFMetAnalyzer, self).declareHandles()
        self.handles['met'] =  AutoHandle(
            'pfMet', 'std::vector<reco::PFMET>'
            )
        self.cleaned_pf_names = ['CleanedTrackerAndGlobalMuons']
        def init_cleaned_pf(label):
            self.handles[label] = AutoHandle(
                ':'.join(['particleFlowTmp',label]), 'std::vector<reco::PFCandidate>'
                )
        map(init_cleaned_pf, self.cleaned_pf_names)
        

    def beginLoop(self, setup):
        super(PFMetAnalyzer,self).beginLoop(setup)

       
    def process(self, event):
        self.readCollections( event.input )
        event.met = self.handles['met'].product()[0]
        print event.met.pt(), event.met.phi(), event.met.sumEt()
        event.CleanedTrackerAndGlobalMuons = self.handles['CleanedTrackerAndGlobalMuons'].product()
        print len(event.CleanedTrackerAndGlobalMuons)
