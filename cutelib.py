#!/usr/bin/python3
# 
# program is usefull for multi media file organisation to ease access
# to available media files and to transcode file when transcoding
# facilitates access.
'''
Program name:  cutelib.py -- python 3.x program is in the current
"cute" directory.  
Copyright 2015 Algis Kabaila,
GPL V2 "copyleft", see file LICENSE in the current directory for
full details.

This program is written in python 3.x programming language.
cutelib.py is a user friendly CLI program with the following arguments:

optional arguments:
-------------------
-h --help    - provide basic help and then quit
-v --verbose - main use to provide more output for debugging
-a --allow   - allow modification of data on disk

positional arguments:
---------------------
segments     - a list of two-tuples of segments of input file
inpath       - path to the directory with input files
outpath      - path to the directory to store output files.  '''

import os
import sys
import argparse
import subprocess
import time

__version__ = '0.0.0 2015-11-28 Canberra'

print('cutelib.py  version ' + __version__)

# Following 2 lines are required work-around to use IDLE
##sys.argv = [sys.argv[0],'-v','-a','segments','inpath','outpath']
sys.argv = [sys.argv[0],'-v'] 
print ('sys.argv = ', sys.argv)

def prolog():
    'Initialise arguments for execution of the program.'
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose',action='store_true',
                        help='Verbose data to help debugging.')
    parser.add_argument('-a','--allow',action='store_true',
                        help='Allow modification of data on disk.')

    parser.add_argument('segments',nargs='?',default=[26, -4],
                        help='26 ch at start, 4 at end remain in file name.')
    parser.add_argument('inpath',nargs='?',default=os.getcwd()+'/data/',
                        help='absolute path to data directory.')
    parser.add_argument('outpath',nargs='?',default=os.getcwd()+'/output/',
                        help='absolute pathe to output directory.')

    args = parser.parse_args()
    if args.verbose:
        print('prolog finished setting up of args.')                
        print('Name space args = ',args)
        return args

def fix_filenames(args):
    ''' Two segments of of old file name makes up the new name - one at the
start of the name, the other at the end of the name. Once the new names are
made, all blanks in the name are replaced by underscore. Contiguous blanks are
replaced by one undersore. File name extensions, indicating the type of file,
are kept unchanged.'''
    verbose  = args.verbose
    allow    = args.allow
    segments = args.segments
    inpath   = args.inpath
    outpath  = args.outpath
    
    print('Namespace args = ', verbose, allow, segments, inpath, outpath)
    # the parameters (paras) will need to be read by this program as data
    videos = 'This is the list of the content of the videos.'
    filenames = os.listdir(inpath)
    videos = 'List of available videos.\n'   
    for v in filenames:
        videos +=  v + '\n'
    print(videos)
#   write out this video list in "output" directory
    print('outpath = ', outpath)
    with open(videos, "w") as f:
        if allow:
            f.write()
# videos = movie program is done
# prepare 'shortnames' a filenames with possibly shorter names.
    shortnames = []
    print('segments = ', segments)
    x1 = int(segments[0])
    x2 = int(segments[1])
    for v in filenames:

        t = v[:x1] + v[x2:]
        print('t = ', t)
        w = ''
        for vv in t.replace('-',' ').split():
            if verbose:               
                print('split vv = ',vv)
            w += (vv+'_') 
             
        shortnames.append(w[:-1])
    print('\n*** shortnames ***\n')
    for short in shortnames:
        print(short)
# finally, do the renaming
    nn = len(shortnames)
    if allow:       
        for i in range(len(shortnames)):
            os.rename(('data/' + filenames[i]), 'data/' + shortnames[i])
    print("Finished up filenames? If not then this is not the end!")   
    return

def transcode(args):
    print('I am callhndb(args)')
    cwd = os.getcwd() 
    print('cwd = ', cwd)
    filenames = os.listdir(cwd + '/data/')
    listinput = []
    for name in filenames:
        if name[-4: ] == '.flv':
            a = "HandBrakeCLI"
            b = cwd + '/data/'   + name
            c = cwd + '/output/' + name + '.mp4'
            print (a, b, c)
            if args.allow:
                subprocess.call([a, "-i", b, "-o", c])
    print('Transcode loop completed')

def main():
    print('main program accessed')
    args = prolog()
    if args.verbose:
        print('Show args in the main = ', args)
# in the example the new name is made up from the old name:
    fix_filenames(args)
    transcode(args)
    return

if __name__=='__main__':
    main()

## todo:
##  Run with '-a' argument and degug
##  record and show time of transcoding

