import FWCore.ParameterSet.Config as cms

process = cms.Process("GEN")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000)
)

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    generator = cms.PSet(
        initialSeed = cms.untracked.uint32(123456789),
        engineName = cms.untracked.string('HepJamesRandom')
    )
)


process.source = cms.Source("EmptySource")
process.load('Colin.PFSim.generators.ee_hzha')
# process.load('Colin.PFSim.generators.genJets_cff')
process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')

process.p = cms.Path(
    process.generator +  
    process.genParticles
    )


# output definition

process.out = cms.OutputModule(
    "PoolOutputModule",
    dataset = cms.untracked.PSet(
    dataTier = cms.untracked.string('GEN')
    ),
    fileName = cms.untracked.string('gen.root'),
    outputCommands = cms.untracked.vstring('keep *')
)

process.outpath = cms.EndPath(process.out)


# process.genJets.verbose = False
