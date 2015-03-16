#ifndef PhysicsTools_Heppy_EGammaMvaEleEstimatorFWLite_h
#define PhysicsTools_Heppy_EGammaMvaEleEstimatorFWLite_h

struct EGammaMvaEleEstimatorCSA14;
namespace reco { struct Vertex; }
namespace pat { struct Electron; }
#include <vector>
#include <string>

namespace heppy {

class EGammaMvaEleEstimatorFWLite {
    public:
        EGammaMvaEleEstimatorFWLite();
        ~EGammaMvaEleEstimatorFWLite();

        enum MVAType {
            kTrigCSA14 = 3, // MVA for non-triggering electrons 
            kNonTrigCSA14 = 4, // MVA for non-triggering electrons 
            kNonTrigPhys14 = 5, // MVA for non-triggering electrons 
        };

        void initialize( std::string methodName,
                MVAType type,
                bool useBinnedVersion,
                std::vector<std::string> weightsfiles );

        float mvaValue(const pat::Electron& ele,
                bool printDebug = false);
    private:
        EGammaMvaEleEstimatorCSA14 *estimatorCSA14_;
};
}
#endif
