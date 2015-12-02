import os
import PhysicsTools.HeppyCore.framework.config as cfg

debug = True

from Colin.MetScanning.samples.pfpaper_nopu import qcd, ttbar
qcd.splitFactor = 10

selectedComponents  = [qcd]

if debug:
    print 'DEBUG MODE !!!'
    selectedComponents = selectedComponents[:1]
    comp = selectedComponents[0]
    comp.files = comp.files[:1]
    comp.splitFactor = 1

from Colin.MetScanning.analyzers.MiniAODReader import MiniAODReader
source = cfg.Analyzer(
    MiniAODReader,
    read_pfcands = False
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
