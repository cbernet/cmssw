import os
import PhysicsTools.HeppyCore.framework.config as cfg

# input component 
# several input components can be declared,
# and added to the list of selected components

#inputSample = cfg.Component(
#    'test_component',
#    files = ['doublemu_miniaod.root'],
#    )

debug = True

from Colin.MetScanning.samples.miniaod import doublemu

selectedComponents  = [doublemu]

if debug:
    print 'DEBUG MODE !!!'
    comp = selectedComponents[0]
    comp.files = comp.files[:200]
    comp.splitFactor = 10


from Colin.MetScanning.analyzers.MiniAODReader import MiniAODReader
source = cfg.Analyzer(
    MiniAODReader,
    )

from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer import JSONAnalyzer
json = cfg.Analyzer(
    JSONAnalyzer
)


from Colin.MetScanning.analyzers.MetAnalyzer import MetAnalyzer
met_ana = cfg.Analyzer(
    MetAnalyzer,
    )

from Colin.MetScanning.analyzers.MetTreeProducer import MetTreeProducer
met_tree = cfg.Analyzer(
    MetTreeProducer,
    tree_name = 'events',
    tree_title = 'MET tree'
    )


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        json,
        source, 
        met_ana,
        met_tree
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
