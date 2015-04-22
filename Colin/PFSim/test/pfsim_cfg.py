import os
import PhysicsTools.HeppyCore.framework.config as cfg

# input component 
# several input components can be declared,
# and added to the list of selected components
inputSample = cfg.Component(
    'albers_example',
    files = ['zqq.root'],
    # files = ['ww.root'],
    # files = ['hz.root'],
    # files = ['ttbar.root'],
    )

selectedComponents  = [inputSample]

from PhysicsTools.HeppyCore.fcc.analyzers.FCCReader import FCCReader
reader = cfg.Analyzer(
    FCCReader
)


from PhysicsTools.HeppyCore.fcc.analyzers.PFSim import PFSim
pfsim = cfg.Analyzer(
    PFSim,
    display = True,
    verbose = False
)


from PhysicsTools.HeppyCore.fcc.analyzers.JetClusterizer import JetClusterizer
jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'rec',
    particles = 'particles'
)

genjets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'gen',
    particles = 'gen_particles_stable'
)

from PhysicsTools.HeppyCore.fcc.analyzers.JetAnalyzer import JetAnalyzer
jetana = cfg.Analyzer(
    JetAnalyzer,
)


from PhysicsTools.HeppyCore.fcc.analyzers.JetTreeProducer import JetTreeProducer
tree = cfg.Analyzer(
    JetTreeProducer,
    tree_name = 'events',
    tree_title = 'jets'
)


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    reader, 
    pfsim,
    jets,
    genjets,
    jetana,
    tree
    ] )

# inputSample.files.append('albers_2.root')
# inputSample.splitFactor = 2  # splitting the component in 2 chunks

# finalization of the configuration object.
from ROOT import gSystem
gSystem.Load("libdatamodel")
from eventstore import EventStore as Events
config = cfg.Config(
    components = selectedComponents,
    sequence = sequence,
    services = [],
    events_class = Events
)

    
if __name__ == '__main__':
    import sys
    from PhysicsTools.HeppyCore.framework.looper import Looper
    import logging

    # next 2 lines necessary to deal with reimports from ipython
    logging.shutdown()
    reload(logging)
    logging.basicConfig(level=logging.ERROR)

    import random
    random.seed(0xdeadbeef)

    
    def process(iev=None):
        if iev is None:
            iev = loop.iEvent
        loop.process(iev)
        if display:
            display.draw()

    def next():
        loop.process(loop.iEvent+1)
        if display:
            display.draw()            

    iev = None
    if len(sys.argv)==2:
        iev = int(sys.argv[1])
    loop = Looper( 'looper', config,
                   nEvents=2000,
                   nPrint=5,
                   timeReport=True)
    pfsim = loop.analyzers[1]
    display = getattr(pfsim, 'display', None)
    simulator = pfsim.simulator
    detector = simulator.detector
    if iev is not None:
        process(iev)
    else:
        loop.loop()
        loop.write()
