import os
import PhysicsTools.HeppyCore.framework.config as cfg

# input component 
# several input components can be declared,
# and added to the list of selected components

#inputSample = cfg.Component(
#    'test_component',
#    files = ['doublemu_miniaod.root'],
#    )

debug = False

comp =  cfg.Component(
    'lucia',
    files = ['Tau_Out.root']
)

selectedComponents  = [comp]


if debug:
    print 'DEBUG MODE !!!'
    comp.files = comp.files[:1]
    comp.splitFactor = 1

from Colin.TauTuple.analyzers.TauAnalyzer import TauAnalyzer
pftaus = cfg.Analyzer(
    TauAnalyzer,
    taus = 'hpsPFTauProducer',
    discs = [ 
        'hpsPFTauDiscriminationByDecayModeFinding',
        'hpsPFTauDiscriminationByMediumIsolation'
        ],
    select_kin = lambda tau: tau.pt()>30.
    )


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        pftaus
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
