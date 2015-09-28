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
    'pf',
    taus = 'hpsPFTauProducer',
    discs = [ 
        'hpsPFTauDiscriminationByDecayModeFindingOldDMs',        
        'hpsPFTauDiscriminationByDecayModeFinding',
        'hpsPFTauMVA3IsolationChargedIsoPtSum',
        'hpsPFTauMVA3IsolationNeutralIsoPtSum',
        'hpsPFTauMVA3IsolationPUcorrPtSum'
        ],
    select_kin = lambda tau: tau.pt()>10. , 
    verbose = False
    )

calotaus = cfg.Analyzer(
    TauAnalyzer,
    'calo',
    taus = 'caloRecoTauProducer',
    discs = [ 
        'caloRecoTauDiscriminationByLeadingTrackFinding',
        'caloRecoTauDiscriminationByLeadingTrackPtCut',
        'caloRecoTauDiscriminationByTrackIsolation',
        'caloRecoTauDiscriminationByIsolation',
        'caloRecoTauDiscriminationByECALIsolation',
        'caloRecoTauDiscriminationAgainstMuon',
        'caloRecoTauDiscriminationAgainstElectron'
        ],
    select_kin = lambda tau: tau.pt()>10. , 
    verbose = False
    )

from Colin.TauTuple.analyzers.TauTreeProducer import TauTreeProducer
pftaus_tree = cfg.Analyzer(
    TauTreeProducer,
    'pf',
    tree_name = 'tau_tree',
    tree_title = 'tau ntuple',
    taus = 'taus_pf',
)

calotaus_tree = cfg.Analyzer(
    TauTreeProducer,
    'calo',
    tree_name = 'tau_tree',
    tree_title = 'tau ntuple',
    taus = 'taus_calo',
)



# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        pftaus,
        pftaus_tree,
        calotaus,
        calotaus_tree
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
