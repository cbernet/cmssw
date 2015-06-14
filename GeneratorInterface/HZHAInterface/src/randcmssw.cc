// #include "GeneratorInterface/Core/interface/RNDMEngineAccess.h"

// #include "CLHEP/Random/RandomEngine.h"
// static CLHEP::HepRandomEngine* randomEngine;

extern "C"{
  double rndmcmssw_(double& dummy){
    //std::cout << "Using CMSSW random number generator" << std::endl;
    //return randomEngine->flat();
    return 0.;
  }
  double pyr_(double& dummy){
    //std::cout << "Using CMSSW random number generator" << std::endl;
    //return randomEngine->flat();
    return 0;
  }  
}  
