#ifndef CommonTools_Utils_TMVAEvaluator_h
#define CommonTools_Utils_TMVAEvaluator_h

#include <memory>
#include <string>
#include <vector>
#include <map>

#include "TMVA/Reader.h"
#include "TMVA/IMethod.h"
#include "CondFormats/EgammaObjects/interface/GBRForest.h"


class TMVAEvaluator {

  public:
    TMVAEvaluator();
    ~TMVAEvaluator();

    void initialize(const std::string & options, const std::string & method, const std::string & weightFile,
                    const std::vector<std::string> & variables, const std::vector<std::string> & spectators, bool useGBRForest=false, bool useAdaBoost=false);
    float evaluate(const std::map<std::string,float> & inputs, bool useSpectators=false);

  private:
    bool mIsInitialized;
    bool mUsingGBRForest;
    bool mUseAdaBoost;

    std::string mMethod;
    std::unique_ptr<TMVA::Reader> mReader;
    std::unique_ptr<TMVA::IMethod> mIMethod;
    std::unique_ptr<const GBRForest> mGBRForest;

    std::map<std::string,std::pair<size_t,float>> mVariables;
    std::map<std::string,std::pair<size_t,float>> mSpectators;
};

#endif // CommonTools_Utils_TMVAEvaluator_h

