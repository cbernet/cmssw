#ifndef __ANALYSISCPP_TOOLS_JETCLUSTERIZER_H__
#define __ANALYSISCPP_TOOLS_JETCLUSTERIZER_H__

#include "TObject.h"
#include "TLorentzVector.h"

#include <vector>

#ifndef __CINT__
#include "fastjet/JetDefinition.hh"
#endif

namespace heppy {

class JetClusterizer {

 public:
  typedef TLorentzVector P4;
  typedef std::vector<P4> Inputs;
  typedef std::vector<P4> Outputs;
  
  JetClusterizer();
  void add_p4(const P4& p4) {m_inputs.push_back(p4);}
  void clusterize();
  void clear() {m_inputs.clear(); m_outputs.clear();}
  
  unsigned n_jets() const {return m_outputs.size();}
  P4  jet(unsigned i) const;

 private:
  Inputs                          m_inputs;
  Outputs                         m_outputs;
#ifndef __CINT__
  fastjet::JetDefinition          m_definition;
#endif
};

}
#endif   
