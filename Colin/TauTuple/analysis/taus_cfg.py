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

#comp =  cfg.Component(
#    'DY',
#    files = ['Tau_Out_DY.root']
#)

from Colin.TauTuple.samples.lucia import mssm 

comp = mssm 
# comp.files = comp.files[:5]
comp.splitFactor = len(comp.files)
selectedComponents  = [comp]


if debug:
    print 'DEBUG MODE !!!'
    comp.files = comp.files[:1]
    comp.splitFactor = 1

from Colin.TauTuple.analyzers.JetReader import JetReader
taugenjets = cfg.Analyzer(
    JetReader, 
    'gentau',
    jets = ('tauGenJets', 'std::vector<reco::GenJet>'),
    jet_pt = 10,
)

pfjets = cfg.Analyzer(
    JetReader, 
    'pfjets',
    jets = ('ak4PFJets', 'std::vector<reco::PFJet>'),
    jet_pt = 10,
)

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
gen_tree = cfg.Analyzer(
    TauTreeProducer,
    'pf',
    tree_name = 'tau_tree',
    tree_title = 'tau ntuple',
    taus = 'gentau',
)

calotaus_tree = cfg.Analyzer(
    TauTreeProducer,
    'calo',
    tree_name = 'tau_tree',
    tree_title = 'tau ntuple',
    taus = 'taus_calo',
)

from Colin.TauTuple.analyzers.Matcher import Matcher                                   
gen2calo = cfg.Analyzer(                                                                     
    Matcher, 
    instance_label = 'calo_gen',
    match_label = 'calo',                                                                         
    match_particles = 'taus_calo',                                                                  
    particles = 'gentau'                                                                        
    ) 

gen2pf = cfg.Analyzer(                                                                     
    Matcher,                  
    instance_label = 'pf_gen',
    match_label = 'pf',                                                                         
    match_particles = 'taus_pf',                                                                  
    particles = 'gentau'                                                                        
    ) 

gen2pfjets = cfg.Analyzer(                                                                     
    Matcher,                    
    instance_label = 'pf_pf',
    match_label = 'pfjet',                                                                         
    match_particles = 'pfjets',                                                                  
    particles = 'gentau'                                                                          
    ) 



# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        taugenjets, 
        pftaus,
        calotaus, 
        pfjets,
        gen2calo,
        gen2pf, 
        gen2pfjets,
        gen_tree,
        # calotaus,
        # calotaus_match_gen,
        # calotaus_tree
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
