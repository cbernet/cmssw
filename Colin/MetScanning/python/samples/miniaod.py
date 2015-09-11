import PhysicsTools.HeppyCore.framework.config as cfg

from getFiles import getFiles 

doublemu = cfg.Component(
    'doublemu',
    files = getFiles(
        "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD", 
        user='CMS', cache=True),
) 



samples = [
    doublemu
]

if __name__ == '__main__':

    import pprint 
    for g in samples:
        print g
