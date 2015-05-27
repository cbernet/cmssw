from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.HeppyCore.statistics.tree import Tree
from Colin.PFSim.analyzers.ntuple import *

from ROOT import TFile

class JetTreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(JetTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'jet_tree.root']),
                              'recreate')
        self.tree = Tree( self.cfg_ana.tree_name,
                          self.cfg_ana.tree_title )
        bookJet(self.tree, 'jet1')
        bookJet(self.tree, 'jet1_pfsim')
        bookJet(self.tree, 'jet1_reco')
        
    def process(self, event):
        if( len(event.gen_jets)>0 ):
            jet = event.gen_jets[0]
            fillJet(self.tree, 'jet1', jet)
            if jet.pfsim:
                fillJet(self.tree, 'jet1_pfsim', jet.pfsim)
            if jet.reco:
                fillJet(self.tree, 'jet1_reco', jet.reco)
        self.tree.tree.Fill()
        
        
    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
        
