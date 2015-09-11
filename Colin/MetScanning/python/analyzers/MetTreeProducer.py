from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.HeppyCore.statistics.tree import Tree
from ntuple import *
from ROOT import TFile

class MetTreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(MetTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'met_tree.root']),
                              'recreate')
        self.tree = Tree( self.cfg_ana.tree_name,
                          self.cfg_ana.tree_title )
        bookMet(self.tree, 'pfmet')
        bookMet(self.tree, 'pfmet_maod_uc')


    def process(self, event):
        self.tree.reset()
        # if hasattr(event, 'eventId'):
        #     fill(self.tree, 'event', event.eventId)
        #     fill(self.tree, 'lumi', event.lumi)
        #     fill(self.tree, 'run', event.run)
        fillMet(self.tree, 'pfmet', event.pfmet)
        fillMet(self.tree, 'pfmet_maod_uc', event.pfmet_maod_uncorr)
        self.tree.tree.Fill()


    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()


