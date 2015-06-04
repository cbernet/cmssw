from ROOT import *

rootfile = 'PhysicsTools.HeppyCore.fcc.analyzers.JetTreeProducer.JetTreeProducer_1/jet_tree.root'

dirs = ['looper_pf', 'looper_calo']
trees = []
files = []

def draw(dir, color, opt=""):
    fname = '/'.join([dir, rootfile])
    tfile = TFile(fname)
    tree = tfile.Get('events')
    trees.append(tree)
    files.append(tfile)
    tree.SetLineColor(color)
    tree.SetLineWidth(2)
    tree.Draw("jet1_e-jet1_gen_e","", opt)
    
draw(dirs[0], 1)
draw(dirs[1], 4, 'same')
