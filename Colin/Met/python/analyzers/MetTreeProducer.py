from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.HeppyCore.statistics.tree import Tree
from ntuple import *
from ROOT import TFile

from MetAnalyzer import pdgids 

class MetTreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(MetTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'met_tree.root']),
                              'recreate')
        self.tree = Tree( self.cfg_ana.tree_name,
                          self.cfg_ana.tree_title )
        for metname in self.cfg_ana.mets:
            bookMet(self.tree, metname)
        bookEvent(self.tree)

    def process(self, event):
        self.tree.reset()
        fillEvent(self.tree, event)
        for metname in self.cfg_ana.mets:
            fillMet(self.tree, metname, getattr(event, metname))
        self.tree.tree.Fill()


    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()

