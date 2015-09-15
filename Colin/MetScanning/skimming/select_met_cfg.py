import FWCore.ParameterSet.Config as cms
import os

##____________________________________________________________________________||
process = cms.Process("LOWMET")

dataset_name = '/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD_1'
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")


##____________________________________________________________________________||
from PhysicsTools.HeppyCore.utils.dataset import createDataset
dataset = createDataset('EOS', 
                        dataset_name , 
                        '.*root', 
                        basedir='/eos/cms/store/cmst3/user/cbern/CMG',
                        readcache=True) 

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        dataset.listOfGoodFiles()
        )
    )

process.lowMet = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("slimmedMETs"),
    cut = cms.string("pt() < 50")
    )

process.lowMetFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("lowMet"),
    minNumber = cms.uint32(1),
  )


process.p = cms.Path(
    process.lowMet + 
    process.lowMetFilter
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

process.e1 = cms.EndPath(
    process.out
    )

print process.source

##____________________________________________________________________________||

