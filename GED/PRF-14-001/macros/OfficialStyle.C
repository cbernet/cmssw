#include <vector>
#include "TStyle.h"
#include "TPad.h"
#include "TCanvas.h"
#include "TLatex.h"
#include "TH1F.h"

void officialStyle() {
    gStyle->SetCanvasColor (0);
    gStyle->SetCanvasBorderSize(10);
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetCanvasDefH (700);
    gStyle->SetCanvasDefW (700);
    gStyle->SetCanvasDefX (100);
    gStyle->SetCanvasDefY (100);
      // color palette for 2D temperature plots
      // gStyle->SetPalette(1,0);
      // Pads
    gStyle->SetPadColor (0);
    gStyle->SetPadBorderSize (10);
    gStyle->SetPadBorderMode (0);

      // Slight modification to keep TPad a square despite relative margins /Juska
    float mb = 0.13;
    float mt = 0.05; 
    float ml = 0.17; 
    float mr = 0.03566265; // mr was 0.05
    gStyle->SetPadBottomMargin(mb);  
    gStyle->SetPadTopMargin (mt);    //    Condition for equal TPad scaling:  
    gStyle->SetPadLeftMargin (ml);   //     (1-mb);(1-mt);/((1-ml);(1-mr);); = 1
    gStyle->SetPadRightMargin (mr);  //     ==> keeping others constant, mr = 0.03566265
    
    gStyle->SetPadGridX (0);
    gStyle->SetPadGridY (0);
    gStyle->SetPadTickX (1);
    gStyle->SetPadTickY (1);
    // Frames
    gStyle->SetLineWidth(3);
    gStyle->SetFrameFillStyle ( 0);
    gStyle->SetFrameFillColor ( 0);
    gStyle->SetFrameLineColor ( 1);
    gStyle->SetFrameLineStyle ( 0);
    gStyle->SetFrameLineWidth ( 2);
    gStyle->SetFrameBorderSize(10);
    gStyle->SetFrameBorderMode( 0);
    // Histograms
    gStyle->SetHistFillColor(2);
    gStyle->SetHistFillStyle(0);
    gStyle->SetHistLineColor(1);
    gStyle->SetHistLineStyle(0);
    gStyle->SetHistLineWidth(3);
    gStyle->SetNdivisions(505);
    // Functions
    gStyle->SetFuncColor(1);
    gStyle->SetFuncStyle(0);
    gStyle->SetFuncWidth(2);
    // Various
    gStyle->SetMarkerStyle(20);
    gStyle->SetMarkerColor(kBlack);
    gStyle->SetMarkerSize (1.4);
    gStyle->SetTitleBorderSize(0);
    gStyle->SetTitleFillColor (0);
    gStyle->SetTitleX (0.2);
    gStyle->SetTitleSize (0.055,"X");
    gStyle->SetTitleOffset(1.100,"X");
    gStyle->SetLabelOffset(0.005,"X");
    gStyle->SetLabelSize (0.050,"X");
    gStyle->SetLabelFont (42 ,"X");
    gStyle->SetStripDecimals(false);
    gStyle->SetLineStyleString(11,"20 10");
    gStyle->SetTitleSize (0.055,"Y");
    gStyle->SetTitleOffset(1.60,"Y");
    gStyle->SetLabelOffset(0.010,"Y");
    gStyle->SetLabelSize (0.050,"Y");
    gStyle->SetLabelFont (42 ,"Y");
    gStyle->SetTextSize (0.055);
    gStyle->SetTextFont (42);
    gStyle->SetStatFont (42);
    gStyle->SetTitleFont (42);
    gStyle->SetTitleFont (42,"X");
    gStyle->SetTitleFont (42,"Y");
    gStyle->SetOptStat (0);
}


void cmsPrel(float lumi, float energy, bool simOnly, bool onLeft=true, float sp=0) {
  TLatex latex;
  
  float t = gStyle->GetPadTopMargin()/(1-sp);
  float tmpTextSize=0.75*t;
  latex.SetTextSize(tmpTextSize);
  latex.SetNDC();
  float textSize=latex.GetTextSize();

  latex.SetName("lumiText");
  latex.SetTextFont(42);

  if (lumi > 0.) {
    latex.SetTextAlign(31); // align left, right=31
    latex.SetTextSize(textSize*0.6/0.75);
    if(lumi > 1000 )
      latex.DrawLatex(0.965,(sp==0)?0.965:0.945,Form(" %.1f fb^{-1} (%.0f TeV)",lumi/1000., energy));
    else
      latex.DrawLatex(0.965,(sp==0)?0.965:0.945,Form(" %.0f pb^{-1} (%.0f TeV)",lumi, energy));
  }
  else {
    latex.SetTextAlign(31); // align right=31
    latex.SetTextSize(textSize*0.6/0.75);
    latex.DrawLatex(0.965,(sp==0)?0.965:0.945,Form(" (%.0f TeV)", energy));
  }
 
  latex.SetTextAlign(onLeft?11:31); // align left / right
  latex.SetTextFont(61);
  latex.SetTextSize(textSize);
  latex.DrawLatex(onLeft?0.204:0.924, (sp==0)?0.893:0.85,"CMS");
  
  latex.SetTextFont(52);
  latex.SetTextSize(textSize*0.76);
  
  if(simOnly)
    latex.DrawLatex(onLeft?0.204:0.924, (sp==0)?0.858:0.8,"Simulation");
  
}

vector<TPad*> getPads(bool ratio, float& splitPad) {

  vector<TPad*> pads;
  
  double bm_ = gStyle->GetPadBottomMargin();  
  double tm_ = gStyle->GetPadTopMargin();
  double lm_ = gStyle->GetPadLeftMargin();
  double rm_ = gStyle->GetPadRightMargin();
  
  if(ratio) {
    splitPad = 0.34;
 
    TPad* pHigh =new TPad("pHigh","pHigh",
			  0., splitPad ,1.,1.);
  
    TPad* pLow  =new TPad("pLow","pLow",
			  0., 0. ,1.,splitPad);

    pHigh->SetLeftMargin(lm_);
    pHigh->SetRightMargin(rm_);
    pHigh->SetTopMargin(tm_/(1-splitPad) );
    pHigh->SetBottomMargin(0.02/(1-splitPad) );
  
    pLow->SetLeftMargin(lm_);
    pLow->SetRightMargin(rm_);
    pLow->SetTopMargin(0.01/splitPad);
    pLow->SetBottomMargin(bm_/splitPad);
  
    pads.push_back(pHigh);
    pads.push_back(pLow);
  } 
  else {
    splitPad = 0;
    TPad* pHigh =new TPad("pHigh","pHigh",
			  0., 0. ,1.,1.);
    
    pHigh->SetLeftMargin(lm_);
    pHigh->SetRightMargin(rm_);
    pHigh->SetTopMargin(tm_);
    pHigh->SetBottomMargin(bm_);
    
    pads.push_back(pHigh);
  }

  return pads;
}


void plotWithRatio(bool ratio=false) {
  officialStyle();
  TCanvas* c=new TCanvas("c","c");
  
  bool simOnly=true;
  float energy=13; //TeV
  float lumi=10000; //pb-1, if 0 no luminosity shown
  bool cmsPrelOnLeft=true;//false put the CMS/simulation text on the right side, to be used only if the left position does not work

  float sp;
  vector<TPad*> pads=getPads(ratio,sp);
  
  //higher pad ==============================================
  c->cd();
  pads[0]->Draw();
  pads[0]->cd();
  
  //draw what you need to draw on higher pad
  TH1F* h=new TH1F("hj","h;some variable [GeV] ; number of events",100,0,100);
  h->GetYaxis()->SetLabelSize( gStyle->GetLabelSize("Y")/(1-sp) );
  h->GetYaxis()->SetTitleSize( gStyle->GetTitleSize("Y")/(1-sp) );
  h->GetYaxis()->SetTitleOffset( gStyle->GetTitleOffset("Y")*(1-sp) );
  if(ratio) {
    h->GetXaxis()->SetLabelSize( 0 );
    h->GetXaxis()->SetTitleSize( 0 );
  }  
  h->Draw();

  //CMS text pad
  cmsPrel(lumi, energy, simOnly, cmsPrelOnLeft,sp);
  




  if(!ratio) return;
  //lower pad ==================================================
  c->cd();
  pads[1]->Draw();
  pads[1]->cd();

  //draw the ratios here ================================
  TH1F* h2=new TH1F("h2","h2;some variable [GeV]; data/MC",100,0,100);
  h2->GetYaxis()->SetLabelSize(gStyle->GetLabelSize("Y")/sp );
  h2->GetXaxis()->SetLabelSize(gStyle->GetLabelSize("X")/sp );
  h2->GetYaxis()->SetTitleSize(gStyle->GetTitleSize("Y")/sp );
  h2->GetXaxis()->SetTitleSize(gStyle->GetTitleSize("X")/sp );
  h2->GetYaxis()->SetTitleOffset(gStyle->GetTitleOffset("Y")*sp );
  h2->GetYaxis()->SetNdivisions(5,5,0);
  h2->GetYaxis()->SetRangeUser(0.71, 1.29 );
  h2->Draw();

}
