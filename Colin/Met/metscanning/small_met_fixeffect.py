from ROOT import TFile, TLegend, TH1, gPad, gDirectory, TCanvas

before = 'SmallMET_nofix'
after = 'SmallMET_fix'

treefile = 'doublemu/Colin.MetScanning.analyzers.MetTreeProducer.MetTreeProducer_1/met_tree.root'

class Plot(object):
    def __init__(self, dirname):
        path = '/'.join([dirname, treefile])
        self.file = TFile(path)
        self.tree = self.file.Get('events')
    def __getattr__(self, attr):
        return getattr(self.tree, attr)

bef = Plot(before)
aft = Plot(after)

aft.SetFillColor(5)
bef.SetFillColor(2)

can = TCanvas("can","", 800, 800)

weight = float(aft.GetEntries())/bef.GetEntries()
bef.Draw('pfmet_pt>>h(100,0,5)', '1*{weight}'.format(weight=weight), 'hist')
aft.Draw('pfmet_pt','','same')
# bef.Draw('pfmet_pt', '1*{weight}'.format(weight=weight), 'histsame')
h = gDirectory.Get('h')
h.SetStats(False)
h.SetTitle(';MET (GeV)')

legend = TLegend(0.5, 0.6, 0.8, 0.8)
legend.AddEntry(bef.tree, 'Before fix', 'f')
legend.AddEntry(aft.tree, 'After fix', 'f')
legend.Draw('same')

gPad.SetLogy()
gPad.Update()
