import FWCore.ParameterSet.Config as cms
import os

##____________________________________________________________________________||
process = cms.Process("RECO2")

json_file = '{cmssw}/src/Colin.Met/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
dataset_name = '/DoubleMuon/Run2015C-PromptReco-v1/RECO'
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")


##____________________________________________________________________________||
from PhysicsTools.HeppyCore.utils.dataset import createDataset
dataset = createDataset('CMS',dataset_name , '.*root', readcache=True) 

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        dataset.listOfGoodFiles()
        )
    )

import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = json_file).getVLuminosityBlockRange()


process.lowMet = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("pfMet"),
    cut = cms.string("pt() < 5")
    )

process.lowMetFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("lowMet"),
    minNumber = cms.uint32(1),
  )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('select.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 100


##____________________________________________________________________________||
process.p = cms.Path(
    process.lowMet + 
    process.lowMetFilter
)

process.e1 = cms.EndPath(
    process.out
    )

print process.source

##____________________________________________________________________________||

