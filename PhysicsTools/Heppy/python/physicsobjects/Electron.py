from PhysicsTools.Heppy.physicsobjects.Lepton import Lepton
from PhysicsTools.Heppy.physicsutils.ElectronMVAID import *
import ROOT

class Electron( Lepton ):

    def __init__(self, *args, **kwargs):
        '''Initializing tightIdResult to None. The user is responsible
        for setting this attribute externally if he wants to use the tightId
        function.'''
        super(Electron, self).__init__(*args, **kwargs)
        self._physObjInit()

    def _physObjInit(self):
        self.tightIdResult = None
        self.associatedVertex = None
        self.rho              = None
        self._mvaRun2 = {}

    def electronID( self, id, vertex=None, rho=None ):
        if id is None or id == "": return True
        if vertex == None and hasattr(self,'associatedVertex') and self.associatedVertex != None: vertex = self.associatedVertex
        if rho == None and hasattr(self,'rho') and self.rho != None: rho = self.rho
        if id.startswith("POG_Cuts_ID_"): 
                return self.cutBasedId(id.replace("POG_Cuts_ID_","POG_")) 
        for ID in self.electronIDs():
            if ID.first == id:
                return ID.second
        raise RuntimeError, "Electron id '%s' not yet implemented in Electron.py" % id

    def cutBasedId(self, wp, showerShapes="auto"):
        if "_full5x5" in wp:
            showerShapes = "full5x5"
            wp = wp.replace("_full5x5","")
        elif showerShapes == "auto":
            if "POG_CSA14_25ns_v1" in wp or "POG_CSA14_50ns_v1" in wp:
                showerShapes = "full5x5"
        vars = {
            'dEtaIn' : abs(self.physObj.deltaEtaSuperClusterTrackAtVtx()),
            'dPhiIn' : abs(self.physObj.deltaPhiSuperClusterTrackAtVtx()),
            'sigmaIEtaIEta' : self.physObj.full5x5_sigmaIetaIeta() if showerShapes == "full5x5" else self.physObj.sigmaIetaIeta(),
            'H/E' : self.physObj.hadronicOverEm(),
            #'1/E-1/p' : abs(1.0/self.physObj.ecalEnergy() - self.physObj.eSuperClusterOverP()/self.physObj.ecalEnergy()),
            '1/E-1/p' : abs(1.0/self.physObj.ecalEnergy() - self.physObj.eSuperClusterOverP()/self.physObj.ecalEnergy()) if self.physObj.ecalEnergy()>0. else 9e9,
        }
        WP = {
            ## ------- https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaCutBasedIdentification?rev=31
            'POG_2012_Veto'   :  [('dEtaIn', [0.007, 0.01]),  ('dPhiIn', [0.8,  0.7 ]), ('sigmaIEtaIEta', [0.01, 0.03]), ('H/E', [0.15, 9e9]), ('1/E-1/p', [9e9,   9e9])],
            'POG_2012_Loose'  :  [('dEtaIn', [0.007, 0.009]), ('dPhiIn', [0.15, 0.1 ]), ('sigmaIEtaIEta', [0.01, 0.03]), ('H/E', [0.12, 0.1]), ('1/E-1/p', [0.05, 0.05])],
            'POG_2012_Medium' :  [('dEtaIn', [0.004, 0.007]), ('dPhiIn', [0.06, 0.03]), ('sigmaIEtaIEta', [0.01, 0.03]), ('H/E', [0.12, 0.1]), ('1/E-1/p', [0.05, 0.05])],
            'POG_2012_Tight'  :  [('dEtaIn', [0.004, 0.005]), ('dPhiIn', [0.03, 0.02]), ('sigmaIEtaIEta', [0.01, 0.03]), ('H/E', [0.12, 0.1]), ('1/E-1/p', [0.05, 0.05])],
            ## ------- https://indico.cern.cH/Event/298242/contribution/1/material/slides/5.pdf (slide 5)
            'POG_CSA14_25ns_v1_Veto'   :  [('dEtaIn', [0.012, 0.015]), ('dPhiIn', [0.8,  0.7 ]), ('sigmaIEtaIEta', [0.01 , 0.033]), ('H/E', [0.15, 9e9 ]), ('1/E-1/p', [9e9,   9e9])],
            'POG_CSA14_25ns_v1_Loose'  :  [('dEtaIn', [0.012, 0.014]), ('dPhiIn', [0.15, 0.1 ]), ('sigmaIEtaIEta', [0.01 , 0.033]), ('H/E', [0.12, 0.12]), ('1/E-1/p', [0.05, 0.05])],
            'POG_CSA14_25ns_v1_Medium' :  [('dEtaIn', [0.009, 0.012]), ('dPhiIn', [0.06, 0.03]), ('sigmaIEtaIEta', [0.01 , 0.031]), ('H/E', [0.12, 0.12]), ('1/E-1/p', [0.05, 0.05])],
            'POG_CSA14_25ns_v1_Tight'  :  [('dEtaIn', [0.009, 0.010]), ('dPhiIn', [0.03, 0.02]), ('sigmaIEtaIEta', [0.01 , 0.031]), ('H/E', [0.12, 0.12]), ('1/E-1/p', [0.05, 0.05])],
            'POG_CSA14_50ns_v1_Veto'   :  [('dEtaIn', [0.012, 0.022]), ('dPhiIn', [0.8,  0.7 ]), ('sigmaIEtaIEta', [0.012, 0.033]), ('H/E', [0.15, 9e9 ]), ('1/E-1/p', [9e9,   9e9])],
            'POG_CSA14_50ns_v1_Loose'  :  [('dEtaIn', [0.012, 0.021]), ('dPhiIn', [0.15, 0.1 ]), ('sigmaIEtaIEta', [0.012, 0.033]), ('H/E', [0.12, 0.12]), ('1/E-1/p', [0.05, 0.05])],
            'POG_CSA14_50ns_v1_Medium' :  [('dEtaIn', [0.009, 0.019]), ('dPhiIn', [0.06, 0.03]), ('sigmaIEtaIEta', [0.01 , 0.031]), ('H/E', [0.12, 0.12]), ('1/E-1/p', [0.05, 0.05])],
            'POG_CSA14_50ns_v1_Tight'  :  [('dEtaIn', [0.009, 0.017]), ('dPhiIn', [0.03, 0.02]), ('sigmaIEtaIEta', [0.01 , 0.031]), ('H/E', [0.12, 0.12]), ('1/E-1/p', [0.05, 0.05])],
        }
        if wp not in WP: 
            raise RuntimeError, "Working point '%s' not yet implemented in Electron.py" % wp
        for (cut_name,(cut_eb,cut_ee)) in WP[wp]:
            if vars[cut_name] >= (cut_eb if self.physObj.isEB() else cut_ee):
                return False
        return True
 
    def absEffAreaIso(self,rho,effectiveAreas):
        '''MIKE, missing doc.
        Should have the same name as the function in the mother class.
        Can call the mother class function with super.
        '''
        return self.absIsoFromEA(rho,self.superCluster().eta(),effectiveAreas.eGamma)

    def mvaId( self ):
        return self.mvaRun2("NonTrigPhys14")
        
    def tightId( self ):
        return self.tightIdResult
    
    def mvaRun2( self, name, debug = False ):
        if name not in self._mvaRun2: 
            if name not in ElectronMVAID_ByName: raise RuntimeError, "Unknown electron run2 mva id %s (known ones are: %s)\n" % (name, ElectronMVAID_ByName.keys())
            self._mvaRun2[name] = ElectronMVAID_ByName[name](self.physObj, debug)
        return self._mvaRun2[name]


    def chargedHadronIsoR(self,R=0.4):
        if   R == 0.3: return self.physObj.pfIsolationVariables().sumChargedHadronPt 
        elif R == 0.4: return self.physObj.chargedHadronIso()
        raise RuntimeError, "Electron chargedHadronIso missing for R=%s" % R

    def neutralHadronIsoR(self,R=0.4):
        if   R == 0.3: return self.physObj.pfIsolationVariables().sumNeutralHadronEt 
        elif R == 0.4: return self.physObj.neutralHadronIso()
        raise RuntimeError, "Electron neutralHadronIso missing for R=%s" % R

    def photonIsoR(self,R=0.4):
        if   R == 0.3: return self.physObj.pfIsolationVariables().sumPhotonEt 
        elif R == 0.4: return self.physObj.photonIso()
        raise RuntimeError, "Electron photonIso missing for R=%s" % R

    def chargedAllIso(self,R=0.4):
        if   R == 0.3: return self.physObj.pfIsolationVariables().sumChargedParticlePt 
        raise RuntimeError, "Electron chargedAllIso missing for R=%s" % R

    def puChargedHadronIsoR(self,R=0.4):
        if   R == 0.3: return self.physObj.pfIsolationVariables().sumPUPt 
        elif R == 0.4: return self.physObj.puChargedHadronIso()
        raise RuntimeError, "Electron chargedHadronIso missing for R=%s" % R


    def dxy(self, vertex=None):
        '''Returns dxy.
        Computed using vertex (or self.associatedVertex if vertex not specified),
        and the gsf track.
        '''
        if vertex is None:
            vertex = self.associatedVertex
        return self.gsfTrack().dxy( vertex.position() )
    def p4(self):	
	 return ROOT.reco.Candidate.p4(self.physObj) 

#    def p4(self):
#        return self.physObj.p4(self.physObj.candidateP4Kind()) # if kind == None else kind)

    def dz(self, vertex=None):
        '''Returns dz.
        Computed using vertex (or self.associatedVertex if vertex not specified),
        and the gsf track.
        '''
        if vertex is None:
            vertex = self.associatedVertex
        return self.gsfTrack().dz( vertex.position() )

    def lostInner(self) :
        if hasattr(self.gsfTrack(),"trackerExpectedHitsInner") :
		return self.gsfTrack().trackerExpectedHitsInner().numberOfLostHits()
	else :	
		return self.gsfTrack().hitPattern().numberOfHits(ROOT.reco.HitPattern.MISSING_INNER_HITS)	

