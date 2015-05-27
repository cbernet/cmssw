import sys
from ROOT import *

rootfile = 'some_aodsim/Colin.PFSim.analyzers.JetTreeProducer.JetTreeProducer_1/jet_tree.root'

dir = sys.argv[1]

fname = '/'.join([dir, rootfile])
tfile = TFile(fname)
tree = tfile.Get('events')


bins = (20, 0, 100)
cut = 'abs(jet1_theta)<0.5'

h_CMS = TH1F("h_CMS", "CMS, #sqrt{s}=91 GeV, e+e- #rightarrow Z #rightarrow ddbar;E_{rec jet} (GeV)", *bins)
h_CMS.Sumw2()
h_PAPAS = TH1F("h_PAPAS", "PFSIM", *bins)
h_PAPAS.Sumw2()

tree.Project("h_CMS", "jet1_reco_e",cut)
tree.Project("h_PAPAS", "jet1_pfsim_e",cut)
 
print 'CMS', '-'*50
h_CMS.Fit("gaus")
print 'PAPAS', '-'*50
h_PAPAS.Fit("gaus")    

h_CMS.SetStats(0)
h_CMS.SetLineWidth(2)
h_CMS.SetLineColor(4)
h_CMS.GetFunction("gaus").SetLineColor(4)
h_PAPAS.SetLineWidth(2)
h_PAPAS.SetLineColor(2)

h_CMS.Draw('')
h_CMS.GetYaxis().SetRangeUser(0, h_CMS.GetMaximum()*1.4)
h_PAPAS.Draw("same")

legend = TLegend(0.51, 0.73, 0.89, 0.89)
legend.AddEntry(h_CMS, "CMS sim and reco")
legend.AddEntry(h_PAPAS, "PAPAS")
legend.Draw()

def print_results(histo, x=None, y=None):
    fun = histo.GetFunction("gaus")
    mean = fun.GetParameter(1)
    dmean = fun.GetParError(1)
    sigma = fun.GetParameter(2)
    dsigma = fun.GetParError(2)
    name = histo.GetName()
    name = name.split('_')[1]
    print name, mean, '+-', dmean
    print name, sigma, '+-', dsigma
    res_str = '{name} mean = {mean:5.1f} #pm{dmean:5.1f}; #sigma = {sigma:5.1f} #pm{dsigma:5.1f}'.format( 
        name=name, 
        mean=mean,
        dmean=dmean, 
        sigma=sigma, 
        dsigma=dsigma)
    latex = TLatex()
    latex.SetNDC()
    latex.DrawLatex(x,y,res_str)

# print_results(h_CMS, 0.5, 0.5)
# print_results(h_PAPAS, 0.5, 0.4)
# gPad.Modified()
# gPad.Update()
