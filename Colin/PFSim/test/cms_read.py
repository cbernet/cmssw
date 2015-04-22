import os
import PhysicsTools.HeppyCore.framework.config as cfg

# input component 
# several input components can be declared,
# and added to the list of selected components
inputSample = cfg.Component(
    'some_aodsim',
    files = ['ee_qq_py_GEN_SIM_RECO.root'],
    )

selectedComponents  = [inputSample]

from Colin.PFSim.analyzers.CMSReader import CMSReader
reader = cfg.Analyzer(
    CMSReader,
    gen_particles = 'genParticles'
)

from Colin.PFSim.analyzers.PFSim import PFSim
pfsim = cfg.Analyzer(
    PFSim,
    display = True,
    verbose = False
)


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    reader, 
    pfsim
    ] )


# finalization of the configuration object.
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
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
