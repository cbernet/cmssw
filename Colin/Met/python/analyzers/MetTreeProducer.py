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
        bookMet(self.tree, 'pfmet')
        for pdgid in pdgids: 
            bookMet(self.tree, 'pfmet_{pdgid}'.format(pdgid=pdgid))
        bookMet(self.tree, 'pfmet_maod_uc')
        bookMet(self.tree, 'pfmet_maod')
        bookMet(self.tree, 'calomet_maod_uc')
        bookEvent(self.tree)

    def process(self, event):
        self.tree.reset()
        fillEvent(self.tree, event)
        if hasattr(event, 'pfmet'):
            fillMet(self.tree, 'pfmet', event.pfmet)
        if hasattr(event, 'pfmets'):
            for pdgid, met in event.pfmets.iteritems():
                fillMet(self.tree, 'pfmet_{pdgid}'.format(pdgid=pdgid), met)
        if hasattr(event, 'pfmet_maod_uc'):
            fillMet(self.tree, 'pfmet_maod_uc', event.pfmet_maod_uc)
        if hasattr(event, 'pfmet_maod'):
            fillMet(self.tree, 'pfmet_maod', event.pfmet_maod)
        if hasattr(event, 'calomet_maod_uc'):
            fillMet(self.tree, 'calomet_maod_uc', event.calomet_maod_uc)
        self.tree.tree.Fill()


    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()

