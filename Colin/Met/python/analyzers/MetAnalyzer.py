from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from Colin.Met.analyzers.MET import METBuilder, METSimple

import math

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
            
        # methods for 7_4_12, miniaod v2 
        # was different in miniaod v1
        # https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#ETmiss
        event.pfmet_maod_uc = METSimple(
            event.maod_met.uncorPt(), 
            event.maod_met.uncorPx(), 
            event.maod_met.uncorPy(), 
            event.maod_met.uncorPhi(), 
            event.maod_met.uncorSumEt(), 
            'pfmet_maod_uc'
            )
        event.pfmet_maod = METSimple(
            event.maod_met.pt(), 
            event.maod_met.px(), 
            event.maod_met.py(), 
            event.maod_met.phi(), 
            event.maod_met.sumEt(), 
            'pfmet_maod'
            )
        # mini aod guys don't store all variables 
        # for calo met.. 
        caloMETPt = event.maod_met.caloMETPt()
        caloMETPhi = event.maod_met.caloMETPhi()
        caloMETPx = caloMETPt*math.cos(caloMETPhi)
        caloMETPy = caloMETPt*math.sin(caloMETPhi)
        event.calomet_maod_uc = METSimple(
            caloMETPt, 
            caloMETPx, 
            caloMETPy, 
            caloMETPhi, 
            event.maod_met.caloMETSumEt(), 
            'calomet_maod'
            )
    
    def sort_pfcands_id(self, cands, ids): 
        sorted_cands = dict()
        for cand in cands:
            pdgid = abs(cand.pdgId())
            if pdgid in ids: 
                sorted_cands.setdefault(pdgid, []).append(cand)
        return sorted_cands
