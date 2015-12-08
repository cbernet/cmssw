import PhysicsTools.HeppyCore.framework.config as cfg
import os
from getFiles import getFiles 

ttbar = cfg.MCComponent(
    'doublemu',
    files = getFiles(
        "/RelValProdTTbar/CMSSW_7_4_0-MCRUN1_74_V4-v1/AODSIM", 
        user='CMS', cache=True),
)



if __name__ == '__main__':

    import pprint 
    pprint.pprint(ttbar.files)
