from ROOT import kBlack, TLatex, TCanvas, TPad

def officialStyle(style):
    style.SetCanvasColor (0)
    style.SetCanvasBorderSize(10)
    style.SetCanvasBorderMode(0)
    style.SetCanvasDefH (700)
    style.SetCanvasDefW (700)
    style.SetCanvasDefX (100)
    style.SetCanvasDefY (100)
    # color palette for 2D temperature plots
    # style.SetPalette(1,0)
    # Pads
    style.SetPadColor (0)
    style.SetPadBorderSize (10)
    style.SetPadBorderMode (0)
    
    style.SetPadBottomMargin(0.13)
    style.SetPadTopMargin (0.05)
    style.SetPadLeftMargin (0.17)
    style.SetPadRightMargin (0.03566265)
    style.SetPadGridX (0)
    style.SetPadGridY (0)
    style.SetPadTickX (1)
    style.SetPadTickY (1)
    # Frames
    style.SetLineWidth(3)
    style.SetFrameFillStyle ( 0)
    style.SetFrameFillColor ( 0)
    style.SetFrameLineColor ( 1)
    style.SetFrameLineStyle ( 0)
    style.SetFrameLineWidth ( 2)
    style.SetFrameBorderSize(10)
    style.SetFrameBorderMode( 0)
    # Histograms
    style.SetHistFillColor(2)
    style.SetHistFillStyle(0)
    style.SetHistLineColor(1)
    style.SetHistLineStyle(0)
    style.SetHistLineWidth(3)
    style.SetNdivisions(505)
    # Functions
    style.SetFuncColor(1)
    style.SetFuncStyle(0)
    style.SetFuncWidth(2)
    # Various
    style.SetMarkerStyle(20)
    style.SetMarkerColor(kBlack)
    style.SetMarkerSize (1.4)
    style.SetTitleBorderSize(0)
    style.SetTitleFillColor (0)
    style.SetTitleX (0.2)
    style.SetTitleSize (0.055,"X")
    style.SetTitleOffset(1.100,"X")
    style.SetLabelOffset(0.005,"X")
    style.SetLabelSize (0.050,"X")
    style.SetLabelFont (42 ,"X")
    style.SetStripDecimals(False)
    style.SetLineStyleString(11,"20 10")
    style.SetTitleSize (0.055,"Y")
    style.SetTitleOffset(1.60,"Y")
    style.SetLabelOffset(0.010,"Y")
    style.SetLabelSize (0.050,"Y")
    style.SetLabelFont (42 ,"Y")
    style.SetTextSize (0.055)
    style.SetTextFont (42)
    style.SetStatFont (42)
    style.SetTitleFont (42)
    style.SetTitleFont (42,"X")
    style.SetTitleFont (42,"Y")
    style.SetOptStat (0)

def cmsPrel(lumi,  energy,  simOnly,  onLeft=True,  sp=0):
    latex = TLatex()
  
    t = gStyle.GetPadTopMargin()/(1-sp)
    tmpTextSize=0.75*t
    latex.SetTextSize(tmpTextSize)
    latex.SetNDC()
    textSize=latex.GetTextSize()

    latex.SetName("lumiText")
    latex.SetTextFont(42)

    lumyloc = 0.965
    cmsyloc = 0.893
    simyloc = 0.858
    if sp!=0:
        lumyloc = 0.945
        cmsyloc = 0.85
        simyloc = 0.8
    cmsalign = 31
    cmsxloc = 0.924
    if onLeft:
        cmsalign = 11
        cmsxloc = 0.204
    if (lumi > 0.):
        latex.SetTextAlign(31) # align left, right=31
        latex.SetTextSize(textSize*0.6/0.75)
        if(lumi > 1000. ):
            latex.DrawLatex(0.965,lumyloc,
                            " {lumi} fb^{{-1}} ({energy} TeV)".format(
                                lumi=lumi/1000.,
                                energy=energy
                            ))
        else:
            latex.DrawLatex(0.965,lumyloc,
                            " {lumi} pb^{{-1}} ({energy} TeV)".format(
                                lumi=lumi,
                                energy=energy
                            ))
  
    else:
        latex.SetTextAlign(31) # align right=31
        latex.SetTextSize(textSize*0.6/0.75)
        latex.DrawLatex(0.965,lumyloc,Form(" (%.0f TeV)", energy))
  
 
    latex.SetTextAlign(cmsalign) # align left / right
    latex.SetTextFont(61)
    latex.SetTextSize(textSize)
    latex.DrawLatex(cmsxloc, cmsyloc,"CMS")
  
    latex.SetTextFont(52)
    latex.SetTextSize(textSize*0.76)
    
    if(simOnly):
        print cmsxloc, simyloc
        latex.DrawLatex(cmsxloc, simyloc,"Simulation")
    
        
class HistStyle:
    def __init__(self,
                 markerStyle = 8,
                 markerColor = 1,
                 markerSize = 1,
                 lineStyle = 1,
                 lineColor = None,
                 lineWidth = 2,
                 fillColor = None,
                 fillStyle = 0 ):
        self.markerStyle = markerStyle
        self.markerColor = markerColor
        self.markerSize = markerSize
        self.lineStyle = lineStyle
        if lineColor is None:
            self.lineColor = markerColor
        else:
            self.lineColor = lineColor
        self.lineWidth = lineWidth
        self.fillColor = fillColor
        self.fillStyle = fillStyle

    def format( self, hist):
        hist.SetMarkerStyle( self.markerStyle )
        hist.SetMarkerColor( self.markerColor )
        hist.SetMarkerSize( self.markerSize )
        hist.SetLineStyle( self.lineStyle )
        hist.SetLineColor( self.lineColor )
        hist.SetLineWidth( self.lineWidth )
        if self.fillColor is not None:
            hist.SetFillColor( self.fillColor )
        hist.SetFillStyle( self.fillStyle )

traditional = HistStyle(markerColor=4, markerStyle=21)
pf = HistStyle(markerColor=2)


class CanvasRatio( TCanvas ):
    '''Produces a canvas with a ratio pad.
    
    The main pad is accessible through self.main
    The ratio pad through self.ratio
    '''
    def __init__(self, name, title, lumi, energy, simOnly):
        super(CanvasRatio, self).__init__(name, title)

        self.lumi = lumi
        self.energy = energy
        self.simOnly = simOnly

        bm_ = gStyle.GetPadBottomMargin()  
        tm_ = gStyle.GetPadTopMargin()
        lm_ = gStyle.GetPadLeftMargin()
        rm_ = gStyle.GetPadRightMargin()
  
        self.splitPad = 0.34
        self.cd()
        self.main = TPad("pMain","pMain",
                         0., self.splitPad ,1.,1.)
        
        self.ratio  = TPad("pRatio","pRatio",
                           0., 0. ,1.,self.splitPad)

        self.main.SetLeftMargin(lm_)
        self.main.SetRightMargin(rm_)
        self.main.SetTopMargin(tm_/(1-self.splitPad) )
        self.main.SetBottomMargin(0.02/(1-self.splitPad) )
        
        self.ratio.SetLeftMargin(lm_)
        self.ratio.SetRightMargin(rm_)
        self.ratio.SetTopMargin(0.01/self.splitPad)
        self.ratio.SetBottomMargin(bm_/self.splitPad)
        self.main.Draw()
        # cmsPrel(25000., 8., True, self.splitPad)
        self.ratio.Draw()

    def draw(self, hist, on_main, *args, **kwargs):
        yaxis = hist.GetYaxis()
        xaxis = hist.GetXaxis()
        if on_main:
            self.main.cd()
            yaxis.SetLabelSize( gStyle.GetLabelSize("Y")/(1-self.splitPad) )
            yaxis.SetTitleSize( gStyle.GetTitleSize("Y")/(1-self.splitPad) )
            yaxis.SetTitleOffset( gStyle.GetTitleOffset("Y")*(1-self.splitPad) )
            xaxis.SetLabelSize( 0 )
            xaxis.SetTitleSize( 0 )
            cmsPrel(self.lumi, self.energy, self.simOnly, True, self.splitPad)
            self.main.Update()
            
        else:
            self.ratio.cd()
            yaxis.SetLabelSize( gStyle.GetLabelSize("Y")/self.splitPad )
            yaxis.SetTitleSize( gStyle.GetTitleSize("Y")/self.splitPad )
            xaxis.SetLabelSize( gStyle.GetLabelSize("Y")/self.splitPad )
            xaxis.SetTitleSize( gStyle.GetTitleSize("Y")/self.splitPad )
            yaxis.SetTitleOffset( gStyle.GetTitleOffset("Y")*self.splitPad )
            yaxis.SetNdivisions(5,5,0)
            yaxis.SetRangeUser(0.71, 1.29)
        hist.Draw(*args, **kwargs)
        self.Update()
            


if __name__ == "__main__":

    from ROOT import gStyle, TH1F, gPad, TLegend

    officialStyle(gStyle)
    h = TH1F("h", "; p_{T} (GeV); a.u.", 10, -5, 5)
    h.Sumw2()
    h.FillRandom("gaus", 1000)
    h.Draw()
    pf.format(h)

    h2 = TH1F("h2", "; p_{T} (GeV); a.u.", 10, -5, 5)
    h2.Sumw2()
    h2.FillRandom("gaus", 1000)
    h2.Draw("same")
    traditional.format(h2)

    legend = TLegend(0.67, 0.71, 0.92, 0.89)
    legend.AddEntry(h, "PF")
    legend.AddEntry(h2, "Traditional")
    legend.Draw()
     
    cmsPrel(25000., 8., True)

    gPad.Update()

    cr  = CanvasRatio('cr', 'canvas with ratio', 25000, 8., True)
    cr.draw(h, True)
    cr.draw(h2, True, 'same')
    
    hratio = h.Clone('hratio')
    hratio.Divide(h2)
    hratio.SetYTitle('ratio')
    cr.draw(hratio, False)

    
