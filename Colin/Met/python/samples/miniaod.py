import PhysicsTools.HeppyCore.framework.config as cfg
import os
from getFiles import getFiles 

doublemu = cfg.DataComponent(
    'doublemu',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD", 
        user='CMS', cache=True),
    json = '{cmssw}/src/Colin.Met/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
) 

doublemu_json =  cfg.DataComponent(
    'doublemu_json',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD_1", 
        user='EOS',basedir='/store/cmst3/user/cbern/CMG', cache=True),
    json = '{cmssw}/src/Colin.Met/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
) 

doublemu_lowmet =  cfg.DataComponent(
    'doublemu_lowmet',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD_1/SmallMET", 
        user='EOS',basedir='/store/cmst3/user/cbern/CMG', cache=True),
    json = '{cmssw}/src/Colin.Met/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
) 

samples = [
    doublemu,
    doublemu_json,
    doublemu_lowmet
]



if __name__ == '__main__':

    import pprint 
    for g in samples:
        print g
