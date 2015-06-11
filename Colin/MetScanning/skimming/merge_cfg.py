import FWCore.ParameterSet.Config as cms

from PhysicsTools.HeppyCore.utils.dataset import EOSDataset

##____________________________________________________________________________||
process = cms.Process("MERGE")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

zerobias1 = EOSDataset('/store/group/phys_jetmet/schoef/private0TSkim_v0/ZeroBias1/crab_ZeroBias1_Run2015A-PromptReco-v1_RECO/150608_144900/0000', '.*root')
zerobias2 = EOSDataset('/store/group/phys_jetmet/schoef/private0TSkim_v0/ZeroBias2/crab_ZeroBias2_Run2015A-PromptReco-v1_RECO/150608_144908/0000', '.*root')
zerobias3 = EOSDataset('/store/group/phys_jetmet/schoef/private0TSkim_v0/ZeroBias3/crab_ZeroBias3_Run2015A-PromptReco-v1_RECO/150608_145006/0000', '.*root')
##____________________________________________________________________________||
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        zerobias3.listOfGoodFiles()
        )
    )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('merge.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))


##____________________________________________________________________________||
process.p = cms.Path()

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||

