import copy

class BaseMET(object):

    def pt(self):
        return self._pt

    def phi(self):
        return self._phi

    def sumEt(self):
        return self._sum_et

    def __str__(self):
        return '{name}/{label}: {pt:7.4f}, {phi:2.4f}, {sum_et:7.0f}'.format(
            label = self.label, 
            name = self.__class__.__name__,
            pt = self.pt(),
            phi = self.phi(), 
            sum_et = self.sumEt())
    

class METBuilder(BaseMET):
 
    def __init__(self, ptcs, label):
        self.ptcs = ptcs 
        self.label = label
        self._p4, self._sum_et = self.compute_met(ptcs)
        self._pt = self._p4.pt()
        self._phi = self._p4.phi()

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


class METSimple(BaseMET): 
    
    def __init__(self, pt, phi, sumet, label):
        self._pt = pt 
        self._phi = phi 
        self._sum_et = sumet
        self.label = label
