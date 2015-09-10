import os
import PhysicsTools.HeppyCore.framework.config as cfg

# input component 
# several input components can be declared,
# and added to the list of selected components
inputSample = cfg.Component(
    'test_component',
    files = ['pickevents_DoubleEG.root'],
    )

selectedComponents  = [inputSample]

from Colin.MetScanning.analyzers.PFMetAnalyzer import PFMetAnalyzer
pfmet_ana = cfg.Analyzer(
    PFMetAnalyzer,
    )


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        pfmet_ana
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
