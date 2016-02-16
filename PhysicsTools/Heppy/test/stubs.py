import os
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.utils.miniAodFiles import miniAodFiles

# set to True if you want several parallel processes
multi_thread = False

# input component 
# several input components can be declared,
# and added to the list of selected components
inputSample = cfg.MCComponent(
    'test_component',
    files=['root://eoscms//eos/cms/store/group/upgrade/Tracker/L1Tracking/Synchro/Input/TTbar/CMSSW_6_2_0_SLHC26-PU_DES23_62_V1_LHCCRefPU200-v1/FE11F646-A418-E511-B1CD-0025905A60A8.root']
    # a list of local or xrootd files can be specified by hand.
    )

if multi_thread: 
    inputSample.splitFactor = len(inputSamples.files)

selectedComponents  = [inputSample]

from PhysicsTools.Heppy.analyzers.objects.StubAnalyzer import StubAnalyzer
stubs = cfg.Analyzer(
    StubAnalyzer,
)

# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [ 
        stubs
        ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from ROOT import gSystem 
gSystem.Load("libDataFormatsL1TrackTrigger")
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config

if __name__ == '__main__':
    # can either run this configuration through heppy, 
    # or directly in python or ipython for easier development. 
    # try: 
    # 
    #   ipython -i simple_example_cfg.py
    # 
    from PhysicsTools.Heppy.physicsutils.LorentzVectors import LorentzVector

    from PhysicsTools.HeppyCore.framework.looper import Looper 
    looper = Looper( 'Loop', config, nPrint = 5, nEvents=100) 
    looper.loop()
    looper.write()

    # and now, let's play with the contents of the event
    print looper.event
    pz = LorentzVector()
    for imu, mu in enumerate(looper.event.muons): 
        print 'muon1', mu, 'abs iso=', mu.relIso()*mu.pt()
        pz += mu.p4()
    print 'z candidate mass = ', pz.M()

    # you can stay in ipython on a given event 
    # and paste more and more code as you need it until 
    # your code is correct. 
    # then put your code in an analyzer, and loop again. 

    def next():
        looper.process(looper.event.iEv+1)
