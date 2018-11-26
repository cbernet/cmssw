from RecoEgamma.ElectronIdentification.FWLite import electron_mvas, working_points
from DataFormats.FWLite import Events, Handle

print('open input file...')

events = Events('root://cms-xrd-global.cern.ch//store/mc/'+ \
        'RunIIFall17MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+ \
        'MINIAODSIM/RECOSIMstep_94X_mc2017_realistic_v10-v1/00000/0293A280-B5F3-E711-8303-3417EBE33927.root')

# Get Handles on the electrons and other products needed to calculate the MVAs
ele_handle  = Handle('std::vector<pat::Electron>')
rho_handle  = Handle('double')
conv_handle = Handle('reco::ConversionCollection')
bs_handle   = Handle('reco::BeamSpot')

print('start processing')

for i,event in enumerate(events): 

    if i == 100:
        break

    event.getByLabel(('slimmedElectrons'),                 ele_handle)
    event.getByLabel(('fixedGridRhoFastjetAll'),           rho_handle)
    event.getByLabel(('reducedEgamma:reducedConversions'), conv_handle)
    event.getByLabel(('offlineBeamSpot'),                  bs_handle)

    electrons = ele_handle.product()
    convs     = conv_handle.product()
    beam_spot = bs_handle.product()
    rho       = rho_handle.product()

    def test_mva(ele, mvaname, convs, beam_spot, rho):
        mva, category = electron_mvas[mvaname](ele, convs, beam_spot, rho)
        wps = working_points[mvaname]
        print '{:<20}, electron, pt={:5.1f}, mva={:5.2f}, cat={:d}'.format(mvaname, ele.pt(), mva, category)
        for wp in wps.working_points:
            print '\t', wp, wps.passed(ele, mva, category, wp)

    for ele in electrons:
        test_mva(ele, 'Fall17IsoV2', convs, beam_spot, rho)
        test_mva(ele, 'Fall17NoIsoV2', convs, beam_spot, rho)
        test_mva(ele, 'Spring16HZZV1', convs, beam_spot, rho)
        test_mva(ele, 'Spring16V1', convs, beam_spot, rho)

