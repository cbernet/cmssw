from Colin.PFSim.particles.particle import Particle as BaseParticle

import math

class Particle(BaseParticle):
    def __init__(self, pdgid, charge, tlv):
        self._pid = pdgid
        self._charge = charge
        self._tlv = tlv
