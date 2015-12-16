import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("TEST")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

##____________________________________________________________________________||
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

##____________________________________________________________________________||
process.load("JetMETCorrections.Type1MET.correctionTermsCaloMet_cff")

##____________________________________________________________________________||
process.load("JetMETCorrections.Type1MET.correctedMet_cff")

##____________________________________________________________________________||
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType1Type2_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType0PFCandidate_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType0RecoTrack_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetMult_cff")

##____________________________________________________________________________||
process.load("JetMETCorrections.Type1MET.correctedMet_cff")

from CondCore.DBCommon.CondDBSetup_cfi import *
import os 
import shutil 

era="PFGED_25nsV1_MC"
fname = era+'.db'
shutil.copy(os.environ['CMSSW_BASE']+'/src/Colin/Met/pfpaper/'+fname, fname)
connectstr = 'sqlite_file:'+os.getcwd()+'/'+fname

process.jec = cms.ESSource(
    "PoolDBESSource",
    CondDBSetup,
    connect = cms.string( connectstr ),
    toGet =  cms.VPSet(
        cms.PSet(
            record = cms.string("JetCorrectionsRecord"),
            tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PF"),
            label= cms.untracked.string("AK4PF")
            ),
        cms.PSet(
            record = cms.string("JetCorrectionsRecord"),
            tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4Calo"),
            label= cms.untracked.string("AK4Calo")
            ),

        #            cms.PSet(
        #                record = cms.string("JetCorrectionsRecord"),
        #                tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PFchs"),
        #                label= cms.untracked.string("AK4PFchs")
        #                ),
        )
    )
process.es_prefer_jec = cms.ESPrefer("PoolDBESSource",'jec')




##____________________________________________________________________________||
from JetMETCorrections.Type1MET.testInputFiles_cff import corrMETtestInputFiles

from Colin.Met.samples.pfpaper_nopu import qcd_reco, ttbar_aod

process.source = cms.Source(
    "PoolSource",
#      fileNames = cms.untracked.vstring("root://eoscms//eos/cms/store/relval/CMSSW_7_4_1/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V9_gensim71X-v1/00000/ACC93B1D-9AEC-E411-919D-0025905A60B8.root")
#    fileNames = cms.untracked.vstring("file:ACC93B1D-9AEC-E411-919D-0025905A60B8.root")
#    fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_4_0/RelValProdTTbar/AODSIM/MCRUN1_74_V4-v1/00000/3C61F496-DEDA-E411-A468-0025905A6134.root')
    fileNames = cms.untracked.vstring(qcd_reco.files)
    )
# process.source.fileNames = process.source.fileNames[:10]

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('corrMET.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep recoPFMETs_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_*_*_TEST'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

##____________________________________________________________________________||
process.p = cms.Path(
    process.correctionTermsCaloMet +
    process.caloMetT1 + 
    process.correctionTermsPfMetType1Type2 +
    process.pfMetT1
)



process.e1 = cms.EndPath(
    process.out
    )

# process.corrCaloMetType1.type1JetPtThreshold = 30.

