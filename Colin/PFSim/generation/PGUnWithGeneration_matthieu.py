# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/SinglePi0E10_cfi.py -s GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,RECO -n 10 --no_exec --conditions=auto:mc
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('Configuration/Generator/python/SinglePi0E10_cfi.py nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    # outputCommands = cms.untracked.vstring("keep *"),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('SinglePi_fullsim.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)
process.RECOSIMoutput.outputCommands.append("keep *_particleFlowSimParticle_*_*")
# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    PGunParameters = cms.PSet(
        PartID = cms.vint32(-211), #PDGID
        MaxEta = cms.double(1.4),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-1.4),
        MinE = cms.double(10),
        MinPhi = cms.double(-3.14159265359),
        MaxE = cms.double(50)
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single pi0 E 10'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)



### ===========================================================
### ZS removal
###
#process.simHcalDigis.useConfigZSvalues=cms.int32(1)
#process.simHcalDigis.HBlevel=cms.int32(-999)
#process.simHcalDigis.HElevel=cms.int32(-999)
#process.simHcalDigis.HOlevel=cms.int32(-999)
#process.simHcalDigis.HFlevel=cms.int32(-999)
#process.simEcalDigis.srpBarrelLowInterestChannelZS = cms.double(-1.e9)
#process.simEcalDigis.srpEndcapLowInterestChannelZS = cms.double(-1.e9)

#process.GlobalTag.toGet = cms.VPSet(
#    cms.PSet(record = cms.string("EcalSRSettingsRcd"),
#             tag = cms.string('EcalSRSettings_fullreadout_v01_mc'),
#             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_34X_ECAL")
#))

###===========================================================

#process.RandomNumberGeneratorService.generator.initialSeed = XXXX
process.RandomNumberGeneratorService.generator.initialSeed = 15279842

process.pfChargedHadronAnalyzer = cms.EDAnalyzer(
    "PFChargedHadronAnalyzer",
    PFCandidates = cms.InputTag("particleFlow"),
    PFSimParticles = cms.InputTag("particleFlowSimParticle"),
    EcalPFClusters = cms.InputTag("particleFlowClusterECAL"),
    HcalPFClusters = cms.InputTag("particleFlowClusterHCAL"),
    ptMin = cms.double(1.),                     # Minimum pt
    pMin = cms.double(1.),                      # Minimum p
    nPixMin = cms.int32(2),                     # Nb of pixel hits
    nHitMin = cms.vint32(14,17,20,17,10),       # Nb of track hits
    nEtaMin = cms.vdouble(1.4,1.6,2.0,2.4,2.6), # in these eta ranges
    hcalMin = cms.double(0.5),                   # Minimum hcal energy
    ecalMax = cms.double(1E9),                  # Maximum ecal energy 
    verbose = cms.untracked.bool(True),         # not used.
    rootOutputFile = cms.string("PGun73X.root"),# the root tree
#    IsMinBias = cms.untracked.bool(False)
)


# Gen Info re-processing
#process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
#process.load("RecoJets.Configuration.GenJetParticles_cff")
#process.load("RecoJets.Configuration.RecoGenJets_cff")
#process.load("RecoMET.Configuration.GenMETParticles_cff")
#process.load("RecoMET.Configuration.RecoGenMET_cff")
process.load("RecoParticleFlow.PFProducer.particleFlowSimParticle_cfi")
#process.load("RecoParticleFlow.Configuration.HepMCCopy_cfi")
process.genReReco = cms.Sequence(#process.generator+
                                 #process.genParticles+
                                 #process.genJetParticles+
                                 #process.recoGenJets+
                                 #process.genMETParticles+
                                 #process.recoGenMET+
                                 process.particleFlowSimParticle)



# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
# process.bla = cms.EndPath(process.pfChargedHadronAnalyzer)
process.blo = cms.EndPath(process.genReReco)
# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.blo, process.RECOSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

