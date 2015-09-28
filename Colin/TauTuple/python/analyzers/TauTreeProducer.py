from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.HeppyCore.statistics.tree import Tree
from ntuple import *
from ROOT import TFile

class TauTreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(TauTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'tau_tree.root']),
                              'recreate')
        self.tree = Tree( self.cfg_ana.tree_name,
                          self.cfg_ana.tree_title )
        self.booked = False

    def process(self, event):
        self.tree.reset()
        taus = getattr(event, self.cfg_ana.taus)
        for tau in taus:
            if not self.booked:
                bookTau(self.tree, self.cfg_ana.taus, tau)
                self.booked = True
            fillTau(self.tree, self.cfg_ana.taus, tau)
            self.tree.tree.Fill()

    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()


