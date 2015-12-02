import PhysicsTools.HeppyCore.framework.config as cfg
import os
from getFiles import getFiles 

qcd = cfg.MCComponent(
    'qcd',
    files = getFiles(
        "/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-AsymptNoPURawReco_MCRUN2_74_V9A-v4/MINIAODSIM", 
        user='CMS', cache=True)
) 

ttbar = cfg.MCComponent(
    'ttbar',
    files = getFiles(
        "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-AsymptNoPU_MCRUN2_74_V9A-v2/MINIAODSIM", 
        user='CMS', cache=True)
) 


if __name__ == '__main__':

    import pprint 
    pprint.pprint(ttbar.files)
