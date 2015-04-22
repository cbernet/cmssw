import math

class Particle(object):
    
    def p4(self):
        return self._tlv

    def p3(self):
        return self._tlv.Vect()

    def e(self):
        return self._tlv.E()

    def pt(self):
        return self._tlv.Pt()
    
    def theta(self):
        return math.pi/2 - self._tlv.Theta()

    def phi(self):
        return self._tlv.Phi()

    def m(self):
        return self._tlv.M()

    def pdgid(self):
        return self._pid

    def q(self):
        return self._charge

    def status(self):
        return self._status
        
    def __str__(self):
        tmp = '{className} : pdgid = {pdgid:3} q = {q:1} e = {e:5.1f}, theta = {theta:5.2f}, phi = {phi:5.2f}, mass = {m:5.2f}'
        return tmp.format(
            className = self.__class__.__name__,
            pdgid = self.pdgid(),
            q = self.q(),
            e = self.e(),
            theta = self.theta(),
            phi = self.phi(),
            m = self.m()
            )
    
