// #include "GeneratorInterface/Core/interface/RNDMEngineAccess.h"

// #include "CLHEP/Random/RandomEngine.h"
// static CLHEP::HepRandomEngine* randomEngine;

#include <cstdlib>
#include <iostream>
#include <ctime>

static bool seeded = false;

// srand((unsigned)time(NULL));

double rand_0_1() {
  if(! seeded) {
    // srand(0xdeadbeef);
    srand((unsigned)time(NULL));
    seeded = true;
  }
  double x=((double)rand()/(double)RAND_MAX);
  return x;
}

extern "C"{
  double rndmcmssw_(double& dummy){
    //std::cout << "Using CMSSW random number generator" << std::endl;
    //return randomEngine->flat();
    return rand_0_1();
  }
  double pyr_(double& dummy){
    //std::cout << "Using CMSSW random number generator" << std::endl;
    //return randomEngine->flat();
    return rand_0_1();
  }  
}  
