import os
import PhysicsTools.HeppyCore.framework.config as cfg

# input component 
# several input components can be declared,
# and added to the list of selected components
# inputSample = cfg.Component(
#     'test_component',
#     files = ['pickevents_DoubleEG.root'],
#     )
from Colin.Met.samples.reco import doublemu_smallmet_fix as comp

selectedComponents  = [comp]
comp.splitFactor = 12

from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer import JSONAnalyzer
json = cfg.Analyzer(
    JSONAnalyzer
)

from Colin.Met.analyzers.PFMetAnalyzer import PFMetAnalyzer
pfmet_ana = cfg.Analyzer(
    PFMetAnalyzer,
    )

from Colin.Met.analyzers.MetTreeProducer import MetTreeProducer
met_tree = cfg.Analyzer(
    MetTreeProducer,
    tree_name = 'events',
    tree_title = 'MET tree'
    )


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        json, 
        pfmet_ana,
        met_tree
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
