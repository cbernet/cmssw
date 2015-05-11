from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.HeppyCore.utils.deltar import matchObjectCollection, deltaR

class JetAnalyzer(Analyzer):

    def process(self, event):
        self.match(event.gen_jets, event.rec_jets, 'pfsim')
        self.match(event.gen_jets, event.pf_jets, 'reco')

    def match(self, jets, jets_to_be_matched, label):
        pairs = matchObjectCollection(jets, jets_to_be_matched, 0.3**2)
        for jet in jets:
            matched = pairs[jet]
            setattr(jet, label, matched)
            # if matched:
            #    jet.dR = deltaR(jet.theta(), jet.phi(),
            #                     jet.gen.theta(), jet.gen.phi())
                # print jet.dR, jet, jet.gen
