from Colin.TauTuple.particles.jet import Jet as BaseJet
from Colin.TauTuple.particles.jet import JetConstituents
from Colin.TauTuple.particles.cms.particle import Particle
from ROOT import TLorentzVector 

class Jet(BaseJet):
    def __init__(self, candidate):
        self.candidate = candidate
        self._pid = candidate.pdgId()
        self._tlv = TLorentzVector()
        p4 = candidate.p4()
        self._tlv.SetPtEtaPhiM(p4.pt(), p4.eta(), p4.phi(), p4.mass())
        self.convert_constituents()

    def convert_constituents(self):
        constits = []
        constits = map(Particle, self.getJetConstituents()) 
        self.constituents = JetConstituents()
        for ptc in constits:
            self.constituents.append(ptc) 

    def __getattr__(self, attr): 
        return getattr(self.candidate, attr)
