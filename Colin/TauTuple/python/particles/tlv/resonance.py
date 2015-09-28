from heppy_fcc.particles.tlv.particle import Particle

class Resonance(Particle):
    """Resonance decaying to two particles (legs).
    
    A leg is a particle-like object with the following methods:
    - q(): returns charge
    - p4(): returns 4-momentum TLorentzVector
    - e(): returns energy

    """
    def __init__(self, leg1, leg2, pid):
        (leg1, leg2) = (leg2, leg1) if leg2.e()>leg1.e() else (leg1, leg2)
        self._leg1 = leg1
        self._leg2 = leg2
        charge = self._leg1.q()+self._leg2.q()
        p4 = self._leg1.p4()+self._leg2.p4()
        super(Resonance, self).__init__(pid,charge,p4)

    def leg1(self):
        """Returns leg with highest energy."""
        return self._leg1

    def leg2(self):
        """Returns leg with lowest energy."""
        return self._leg2
