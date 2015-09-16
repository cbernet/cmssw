

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from Colin.MetScanning.analyzers.MET import METBuilder, METSimple

pdgids = [211,22,130,1,2]

class MetAnalyzer( Analyzer ):

    def declareHandles(self):
        super(MetAnalyzer, self).declareHandles()
        

    def beginLoop(self, setup):
        super(MetAnalyzer,self).beginLoop(setup)

       
    def process(self, event):
        if hasattr(event, 'pfcands'):
            pfcands = event.pfcands
            event.pfmet = METBuilder(pfcands, 'pf_all')
            sorted_cands = self.sort_pfcands_id(pfcands, pdgids)
            event.pfmets = dict()
            for pdgid, cands in sorted_cands.iteritems():
                met = METBuilder(cands, 'pf_{pdgid}'.format(pdgid=pdgid))
                event.pfmets[pdgid] = met
                # setattr(event, 'pfmet_{pdgid}'.format(pdgid=pdgid), met) 
            
            # import pdb; pdb.set_trace()

        event.pfmet_maod_uncorr = METSimple(event.maod_met.uncorrectedPt(), 
                                            event.maod_met.uncorrectedPhi(), 
                                            event.maod_met.uncorrectedSumEt(), 
                                            'pfmet_maod_uncorr')
    
    def sort_pfcands_id(self, cands, ids): 
        sorted_cands = dict()
        for cand in cands:
            pdgid = abs(cand.pdgId())
            if pdgid in ids: 
                sorted_cands.setdefault(pdgid, []).append(cand)
        return sorted_cands
