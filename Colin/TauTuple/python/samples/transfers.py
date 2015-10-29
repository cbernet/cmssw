import os
import PhysicsTools.HeppyCore.utils.eostools as eostools

def read_lfns(lfns_name):
    ifile = open(lfns_name)
    lfns = []
    for line in ifile:
        line = line.rstrip()
        if line.startswith('/store') and line.endswith('.root'):
            lfns.append(line)
        else: 
            print 'corrupted line:', line
    return lfns

def prepare_destdir(destination):
    try: 
        eostools.mkdir(destination)
    except OSError: 
        # not very clean, just keep going if dir exists...
        pass

def copy_lfn(lfn):
    cpstr = 'xrdcp {source}{lfn} {destination}/{fname}'.format(
        source = source,
        destination = destination,
        lfn = lfn, 
        fname = os.path.basename(lfn)
        )
    print cpstr
    os.system(cpstr)

if __name__ == '__main__':

    import sys 

    if len(sys.argv)!=4:
        print 'usage <list of LFNs> <source xrootd address> <destination xrootd address>'
        sys.exit(1)

    lfns_fname, source, destination = sys.argv[1:]
    # source = source.rstrip('/')
    destination = destination.rstrip('/')

    lfns = read_lfns(lfns_fname)

    print 'files:'
    print lfns
    print 'source', source
    print 'destination', destination

    prepare_destdir(destination)
    map(copy_lfn, lfns)


# xrdcp root://xrootd-cms.infn.it//store/user/lperrini/SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/151019_123821/0000/output_10.root .

# xrdcp 
# root://xrootd-cms.infn.it//store/user/lperrini//SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/crab_NtupleSUSY/150929_112527/0000/output_10.root 
# root://eoscms.cern.ch//eos/cms/store/cmst3/user/cbern/MyTests/
