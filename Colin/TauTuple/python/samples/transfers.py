


if __name__ == '__main__':

    import sys 

    if len(sys.argv)!=2:
        print 'usage <list of filenames> <destination LFN>'
    input_fnames, output_dir = sys.argv

    print 'copy'
    print input_fnames
    print 'destination', output_dir
