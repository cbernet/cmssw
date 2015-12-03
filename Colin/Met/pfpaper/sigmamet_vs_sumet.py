import sys 
import numpy as np
from cpyroot import *

rootfile = TFile(sys.argv[1])
tree = rootfile.Get('events')

class MetVsSumEt(object): 
    def __init__(self, metname, tree, nx, xmin, xmax, ny, ymin, ymax):
        self.metname = metname
        hname = '{metname}_h2d'.format(metname = metname)
        self.h2d = TH2F(hname, hname, 
                        nx, xmin, xmax, ny, ymin, ymax)
        tree.Project(self.h2d.GetName(), 
                     '{metname}_px:{metname}_sumet'.format(metname=metname))
        fr = []
        for ibin in range(self.h2d.GetNbinsX()):
            bin = ibin+1
            fr.append( self.fit(bin) )
        self.fit_results = np.array(fr, dtype=np.float64)
        # import pdb; pdb.set_trace()
        self.gmean = TGraphErrors( 
            len(self.fit_results),
            self.fit_results[:,0].flatten(), 
            self.fit_results[:,2].flatten(),
            self.fit_results[:,1].flatten(), 
            self.fit_results[:,3].flatten()
            )

    def draw2D(self, *args):
        self.h2d.Draw(*args)
        self.gmean.Draw('psame')

    def fit(self, bin, opt='0'): 
        hslice = self.h2d.ProjectionY("", bin, bin, "")
        if not hslice.GetEntries(): 
            return 0., 0., 0., 0., 0., 0.
        hslice.Fit('gaus', opt)
        func = hslice.GetFunction('gaus')
        # import pdb; pdb.set_trace()
        x = self.h2d.GetXaxis().GetBinCenter(bin)
        dx = self.h2d.GetXaxis().GetBinWidth(bin)
        mean = func.GetParameter(1)
        dmean = func.GetParError(1)
        sigma = func.GetParameter(2)
        dsigma = func.GetParError(2)
        return x, dx, mean, dmean, sigma, dsigma
        

metpf = MetVsSumEt('pfmet_maod', tree, 10, 0, 100, 100, -100, 100) 
metpf.draw2D('colz')

# calo = MetVsSumEt('calomet_maod_uc', tree, 10, 0, 100, 100, -100, 100) 
# calo.draw2D('colz')

# bin = 10
# hslice = pf.h2d.ProjectionY("", bin, bin, "")
# hslice.Fit('gaus', '0')
# func = hslice.GetFunction('gaus')
# mean = func.GetParameter(1)
# dmean = func.GetParError(1)
# sigma = func.GetParameter(2)
# dsigma = func.GetParError(2)
# print mean, sigma
