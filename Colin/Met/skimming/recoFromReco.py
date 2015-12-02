# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --datatier AODSIM --process reRECO --conditions auto:run1_mc --filtername RECOfromRECO -s RECO,EI --eventcontent AODSIM --no_exec -n 100 --filein file:step3.root --fileout file:step4.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('reRECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200)
)

from PhysicsTools.HeppyCore.utils.dataset import createDataset

ds = createDataset( 'cbern', '/DoubleMuon/Run2015C-PromptReco-v1/RECO/RECO_SmallMET', '.*root',
                    readcache=True)
non_empty_files = []
for fname, status in ds.report['Files'].iteritems():
    if status[1]:
        non_empty_files.append(str(fname))

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(non_empty_files),
    secondaryFileNames = cms.untracked.vstring()
)

# from PhysicsTools.HeppyCore.utils.datasetToSource import datasetToSource
# process.source = datasetToSource("cbern", "/DoubleMuon/Run2015C-PromptReco-v1/RECO/RECO_SmallMET",
#                                 readCache=False)



process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('RECOfromRECO')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:rereco.root'),
#    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v1'

#process.particleFlowTmp.verbose = cms.untracked.bool(True)
#process.particleFlowTmp.debug   = cms.untracked.bool(True)

# Path and EndPath definitions
process.reconstruction_step = cms.Path(process.reconstruction_fromRECO)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.reconstruction_step,process.eventinterpretaion_step,process.endjob_step,process.AODSIMoutput_step)



