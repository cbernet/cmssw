from PhysicsTools.HeppyCore.utils.dataset import createDataset

def getFiles(dataset, cache=True, user='EOS', basedir='/store/cmst3/user/cbern/CMG'):
    ds = createDataset(user, dataset, '.*root', 
                       readcache=cache, basedir=basedir)
    filenames = ds.listOfGoodFiles()
    if ds.report:
        non_empty_files = []
        for fname, status in ds.report['Files'].iteritems():
            if status[1]:
                non_empty_files.append(str(fname))
        filenames = non_empty_files
    return ['root://eoscms.cern.ch//eos/cms{fname}'.format(fname=fname) 
            for fname in filenames]

