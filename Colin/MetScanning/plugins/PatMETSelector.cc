#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/StringCutObjectSelector.h"
#include "CommonTools/UtilAlgos/interface/SingleObjectSelector.h"
#include "DataFormats/PatCandidates/interface/MET.h"

namespace colin {
  namespace modules {
    typedef SingleObjectSelector<
              pat::METCollection,
              StringCutObjectSelector<pat::MET>
            > PatMETSelector;

DEFINE_FWK_MODULE( PatMETSelector );

  }
}
