import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter(
    "Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            # 'pythia8CUEP8M1Settings', 
            'processParameters'),
        processParameters = cms.vstring(
            'Beams:eCM = 91.',
            'WeakSingleBoson:all = on',
            'WeakZ0:gmZmode = 0',
            'PhaseSpace:pTHatMin = 20.',
            '23:onMode = off',
            '23:onIfMatch = 1 1'),
        # pythia8CUEP8M1Settings = cms.vstring(
        #     'Tune:pp 14', 
        #     'Tune:ee 7', 
        #     'MultipartonInteractions:pT0Ref=2.4024', 
        #     'MultipartonInteractions:ecmPow=0.25208', 
        #     'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring(
            'Beams:idA = 11', 
            'Beams:idB = -11', 
            # 'Tune:preferLHAPDF = 2', 
            # 'Main:timesAllowErrors = 10000', 
            # 'Check:epTolErr = 0.01', 
            # 'Beams:setProductionScalesFromLHEF = off', 
            # 'SLHA:keepSM = on', 
            # 'SLHA:minMassSM = 1000.', 
            # 'ParticleDecays:limitTau0 = on', 
            # 'ParticleDecays:tau0Max = 10', 
            # 'ParticleDecays:allowPhotonRadiation = on'
            )
    ),
    comEnergy = cms.double(91.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)
