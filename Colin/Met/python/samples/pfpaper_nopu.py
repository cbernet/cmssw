import PhysicsTools.HeppyCore.framework.config as cfg
import os
import glob
from getFiles import getFiles 

qcd = cfg.MCComponent(
    'qcd',
    files = getFiles(
        "/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-AsymptNoPURawReco_MCRUN2_74_V9A-v4/MINIAODSIM", 
        user='CMS', cache=True)
) 


qcd_reco = cfg.MCComponent(
    'qcd_reco',
    files = []
)
qcd_reco_sample = '/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-AsymptNoPURawReco_MCRUN2_74_V9A-v4/GEN-SIM-RECO'
qcd_reco_blocks = [
    '05cb984c-1508-11e5-9f48-a0369f23cf8a',
    '03adb124-1505-11e5-a247-001e67abf518',
    '03aa7784-1505-11e5-a247-001e67abf518',
    '19d03b0e-1503-11e5-9f48-a0369f23cf8a'
]
for block in qcd_reco_blocks:
    qcd_reco.files.extend( getFiles('#'.join([qcd_reco_sample, block]),
                                    user='CMS', cache=True) )

qcd_small_8dec = cfg.MCComponent(
    'qcd_small_8dec',
    # files = glob.glob('QCD_small_8dec/Job_*/*.root')
    files = glob.glob('QCD_small_bcd7015/Job_*/*.root')
    )

ttbar_aod = cfg.MCComponent(
    'ttbar',
    files = getFiles(
        "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-AsymptNoPU_MCRUN2_74_V9A-v2/AODSIM", 
        user='CMS', cache=True)
) 


if __name__ == '__main__':

    import pprint 
    sample = qcd_reco
    pprint.pprint(sample.files)
    print len(sample.files
)
