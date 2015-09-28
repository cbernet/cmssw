from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from DataFormats.FWLite import Handle

events = Events('Tau_Out.root', 'Events')

h_pf  = Handle ('std::vector<reco::PFTau>')
h_pfdisc = Handle('reco::PFTauDiscriminator')

for i, event in enumerate(events): 
    print 'event', i
    if i == 10:
        break
    event.getByLabel('hpsPFTauProducer', h_pf)
    event.getByLabel('hpsPFTauDiscriminationByDecayModeFinding', h_pfdisc)
    pftaus = h_pf.product()
    pftaudisc = h_pfdisc.product()
    for itau, tau in enumerate(pftaus):
        print tau.pt(), pftaudisc[itau].second
