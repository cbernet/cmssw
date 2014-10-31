import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8GeneratorFilter",
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(1.293e05),
        filterEfficiency = cms.untracked.double(1),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(0),

        PythiaParameters = cms.PSet(
                processParameters = cms.vstring(
                        'Main:timesAllowErrors    = 10000',
                        'ParticleDecays:limitTau0 = on',
                        'ParticleDecays:tauMax = 10',
                        'Tune:pp 5',
                        'Tune:ee 3',
                        'WeakZ0:gmZmode 0',
                        'WeakSingleBoson:ffbar2gmZ',
                        '22:onMode = off',
                        '22:onIfAny = 13,13',
                        '23:onMode = off',
                        '23:onIfAny = 13,13'

                ),
                parameterSets = cms.vstring('processParameters')
        )
)
