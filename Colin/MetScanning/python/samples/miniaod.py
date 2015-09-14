import PhysicsTools.HeppyCore.framework.config as cfg
import os
from getFiles import getFiles 

doublemu = cfg.DataComponent(
    'doublemu',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD", 
        user='CMS', cache=True),
    json = '{cmssw}/src/Colin/MetScanning/python/samples/vince_25ns.json'.format(cmssw=os.environ['CMSSW_BASE'])
) 



samples = [
    doublemu
]



if __name__ == '__main__':

    import pprint 
    for g in samples:
        print g
