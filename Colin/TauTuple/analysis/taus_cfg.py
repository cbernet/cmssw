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

from Colin.TauTuple.samples.lucia import mssm, ztautau, qcd

comp = qcd
# comp.files = comp.files[:5]
comp.splitFactor = len(comp.files)
selectedComponents  = [comp]

genjets_collection = 'tauGenJets'
if 'qcd' in comp.name.lower():
    genjets_collection = 'ak4GenJetsNoNu'

if debug:
    print 'DEBUG MODE !!!'
    comp.files = comp.files[:1]
    comp.splitFactor = 1

from Colin.TauTuple.analyzers.JetReader import JetReader
genjets = cfg.Analyzer(
    JetReader, 
    'gen',
    jets = (genjets_collection, 'std::vector<reco::GenJet>'),
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
    taus = 'gen',
)


from Colin.TauTuple.analyzers.Matcher import Matcher                                   
gen2calo = cfg.Analyzer(                                                                     
    Matcher, 
    instance_label = 'calo_gen',
    match_label = 'calo',                                                                         
    match_particles = 'taus_calo',                                                                  
    particles = 'gen'                                                                        
    ) 

gen2pf = cfg.Analyzer(                                                                     
    Matcher,                  
    instance_label = 'pf_gen',
    match_label = 'pf',                                                                         
    match_particles = 'taus_pf',                                                                  
    particles = 'gen'                                                                        
    ) 

gen2pfjets = cfg.Analyzer(                                                                     
    Matcher,                    
    instance_label = 'pf_pf',
    match_label = 'pfjet',                                                                         
    match_particles = 'pfjets',                                                                  
    particles = 'gen'                                                                          
    ) 



# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
        genjets, 
        pftaus,
        calotaus, 
        pfjets,
        gen2calo,
        gen2pf, 
        gen2pfjets,
        gen_tree,
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config
