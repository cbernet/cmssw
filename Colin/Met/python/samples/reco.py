import PhysicsTools.HeppyCore.framework.config as cfg
import os
from getFiles import getFiles 

doublemu_smallmet = cfg.DataComponent(
    'doublemu',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/RECO/RECO_SmallMET", 
        user='cbern', cache=True),
    json = '{cmssw}/src/Colin.Met/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
) 

doublemu_smallmet_fix = cfg.DataComponent(
    'doublemu',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/RECO/RECO_SmallMET/METFIX_TestProd", 
        user='cbern', cache=True),
    json = '{cmssw}/src/Colin.Met/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
) 

samples = [
    doublemu_smallmet,
    doublemu_smallmet_fix
]



if __name__ == '__main__':

    import pprint 
    for g in samples:
        print g
