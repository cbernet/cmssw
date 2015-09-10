
import copy
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject as PFCandidate

class MET(object):
 
    def __init__(self, ptcs, label):
        self.ptcs = ptcs 
        self.label = label
        self.p4, self.sum_et = self.compute_met(ptcs)

    def compute_met(self, ptcs):
        sum_p4 = None
        sum_et = 0
        for ptc in ptcs:
            sum_et += ptc.pt()
            if sum_p4 is None:
                sum_p4 = copy.copy(ptc.p4())
            else:
                sum_p4 += ptc.p4()
        met_p4 = - sum_p4
        return met_p4, sum_et

    def pt(self):
        return self.p4.pt()

    def phi(self):
        return self.p4.phi()

    def sumEt(self):
        return self.sum_et

    def __str__(self):
        return '{name}/{label}: {pt:7.4f}, {phi:2.4f}, {sum_et:7.0f}'.format(
            label = self.label, 
            name = self.__class__.__name__,
            pt = self.pt(),
            phi = self.phi(), 
            sum_et = self.sumEt())

class PFMetAnalyzer( Analyzer ):

    def declareHandles(self):
        super(PFMetAnalyzer, self).declareHandles()
        self.handles['met'] =  AutoHandle(
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
        event.met = self.handles['met'].product()[0]
        print 'PFMET', event.met.pt(), event.met.phi(), event.met.sumEt()
        #         event.CleanedTrackerAndGlobalMuons = self.handles['CleanedTrackerAndGlobalMuons'].product()
        #     print len(event.CleanedTrackerAndGlobalMuons)
        for name in self.cleaned_pf_names:
            coll = map(PFCandidate, self.handles[name].product())
            print name, len(coll)
            setattr(event, name, coll)

        event.pf = map(PFCandidate, self.handles['pf'].product())
        print 'pf', len(event.pf)
        event.rec_pfmet = MET(event.pf, 'particleFlow')
        print event.rec_pfmet

