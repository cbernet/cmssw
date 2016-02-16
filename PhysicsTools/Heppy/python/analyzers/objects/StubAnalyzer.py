from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle

class StubAnalyzer(Analyzer):

    def declareHandles(self):
        super(StubAnalyzer, self).declareHandles()
        crazy_type = 'edmNew::DetSetVector< TTStub< edm::Ref<edm::DetSetVector<PixelDigi>,PixelDigi,edm::refhelper::FindForDetSetVector<PixelDigi> >  > >'
        self.handles['stubs'] = AutoHandle( ('TTStubsFromPixelDigis','StubAccepted'),
                                            crazy_type)

    def process(self, event):
        super(StubAnalyzer, self).readCollections(event.input)
        stubs = self.handles['stubs'].product()
        print '#stubs:', len(stubs)
        # jets = self.handles['genjets'].product()
        # for j in jets: 
        #    print j.pt()
