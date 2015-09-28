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

    def eta(self):
        return self._tlv.Eta()

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

    def start_vertex(self):
        return self._start_vertex 

    def end_vertex(self):
        return self._end_vertex

    def __str__(self):
        tmp = '{className} : pdgid = {pdgid:5}, status = {status:3}, q = {q:2} e = {e:5.1f}, theta = {theta:5.2f}, phi = {phi:5.2f}, mass = {m:5.2f}'
        return tmp.format(
            className = self.__class__.__name__,
            pdgid = self.pdgid(),
            status = self.status(),
            q = self.q(),
            e = self.e(),
            theta = self.theta(),
            phi = self.phi(),
            m = self.m()
            )
    
