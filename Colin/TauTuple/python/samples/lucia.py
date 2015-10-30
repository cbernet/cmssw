import PhysicsTools.HeppyCore.framework.config as cfg
import os
from getFiles import getFiles 

mssm = cfg.Component(
    'mssm',
    files = getFiles(
        "/SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY", 
        user='EOS', cache=True),
    ) 

ztautau = cfg.Component(
    'ztt',
    files = getFiles(
        "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_NtupleDY/150929_111739", 
        user='cbern', cache=True),
    ) 

qcd = cfg.Component(
    'qcd',
    files = getFiles(
        "/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/crab_NtupleQCD/150929_103656", 
        user='cbern', cache=True),
    ) 


def xrd(fname):
    return '/'.join(['root://xrootd-cms.infn.it//store/user/lperrini',
                     fname])

mssm_files = [
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_10.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_11.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_12.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_13.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_14.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_1.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_2.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_3.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_4.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_5.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_6.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_7.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_8.root',
'SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_9.root',
]

mssm_louvain = cfg.Component(
    'mssm_louvain',
    files = map(xrd, mssm_files)
) 


if __name__ == '__main__':
    
    for f in qcd.files:
        print f
