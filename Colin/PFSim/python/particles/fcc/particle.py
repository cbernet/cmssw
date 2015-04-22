from Colin.PFSim.particles.particle import Particle as BaseParticle
from ROOT import TLorentzVector
import math

class Particle(BaseParticle):
    def __init__(self, fccptc):
        self.fccptc = fccptc
        self._charge = fccptc.read().Core.Charge
        self._pid = fccptc.read().Core.Type
        self._status = fccptc.read().Core.Status
        self._tlv = TLorentzVector()
        p4 = fccptc.read().Core.P4
        self._tlv.SetPtEtaPhiM(p4.Pt, p4.Eta, p4.Phi, p4.Mass)
        
