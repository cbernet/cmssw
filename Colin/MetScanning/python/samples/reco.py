import PhysicsTools.HeppyCore.framework.config as cfg
import os
from getFiles import getFiles 

doublemu_smallmet = cfg.DataComponent(
    'doublemu',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/RECO/RECO_SmallMET", 
        user='cbern', cache=True),
    json = '{cmssw}/src/Colin/MetScanning/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
) 

samples = [
    doublemu_smallmet
]



if __name__ == '__main__':

    import pprint 
    for g in samples:
        print g
