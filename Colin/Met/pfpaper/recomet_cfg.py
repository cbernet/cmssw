import os
import PhysicsTools.HeppyCore.framework.config as cfg

debug = False

from Colin.Met.samples.pfpaper_nopu import qcd_small_8dec as qcd

selectedComponents  = [qcd]

if debug:
    print 'DEBUG MODE !!!'
    selectedComponents = selectedComponents[:1]
    comp = selectedComponents[0]
    comp.files = comp.files[:1]
    comp.splitFactor = 1

from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer import JSONAnalyzer
json = cfg.Analyzer(
    JSONAnalyzer
)

from Colin.Met.analyzers.RecoMetReader import RecoMetReader
pfmet = cfg.Analyzer(
    RecoMetReader,
    met = ('std::vector< reco::PFMET >', 'pfMet')
    )
pfmetcor = cfg.Analyzer(
    RecoMetReader,
    met = ('std::vector< reco::PFMET >', 'pfMetT1')
    )
calomet = cfg.Analyzer(
    RecoMetReader,
    met = ('std::vector< reco::CaloMET >', 'caloMet')
    )
calometcor = cfg.Analyzer(
    RecoMetReader,
    met = ('std::vector< reco::CaloMET >', 'caloMetT1')
    )


from Colin.Met.analyzers.MetTreeProducer import MetTreeProducer
met_tree = cfg.Analyzer(
    MetTreeProducer,
    tree_name = 'events',
    tree_title = 'MET tree',
    mets = ('pfMet', 'pfMetT1', 'caloMet', 'caloMetT1')
    )


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        json,
        pfmet, 
        pfmetcor,
        calomet,
        calometcor,
        met_tree
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
