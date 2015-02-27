# Copyright (C) 2014 Colin Bernet
# https://github.com/cbernet/heppy/blob/master/LICENSE

from ROOT import TFile, TChain

class Events(object):
    '''Event list from a tree in a root file.
    '''
    def __init__(self, filename, treename, options=None):

        #If provided with a list, use TChain
        if not isinstance(filename, str) and isinstance(filename, list):
            self.file = filename
            self.tree = TChain(treename)
            for fn in filename:
                self.tree.AddFile(fn)
        #If single file, use TFile.Open
        elif isinstance(filename, str):
            self.file = TFile.Open(filename)
            if self.file.IsZombie():
                raise ValueError('file {fnam} does not exist'.format(fnam=filename))
            self.tree = self.file.Get(treename)
        else:
            raise ValueError("filename should be str or list of str but is {0}".format(filename))

        if self.tree == None: # is None would not work
            raise ValueError('tree {tree} does not exist in file {fnam}'.format(
                tree = treename,
                fnam = filename
                ))

    def size(self):
        return self.tree.GetEntries()

    def to(self, iEv):
        '''navigate to event iEv.'''
        self.tree.GetEntry(iEv)
        return self.tree

    def __iter__(self):
        return iter(self.tree)

    def __len__(self):
        return self.size()

    def __getitem__(self, i):
        self.tree.GetEntry(i)
        return self.tree

if __name__ == '__main__':

    import sys
    events = Events(sys.argv[1], 'test_tree')
    print '\naccessing one event directly'
    event = events.to(2)
    print event.var1
    print '\nlooping on all events:'
    for iev, ev in enumerate(events):
         if iev==9:
             print '...'
         if iev>=9 and iev<990:
             continue
         else:
             print ev.var1
