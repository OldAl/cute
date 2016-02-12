#!/usr/bin/python3
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
-a --allow   - allow transcoding and modification of data on disk

positional arguments:
---------------------
segments     - a list of limits of segments of input file
inpath       - path to the directory with input files
outpath      - path to the directory to store output files.  '''

import os
import sys
import argparse
import subprocess
import time
import shutil

__version__ = '0.0.5   2016-02-07 Canberra'

print('cutelib.py  version ' + __version__)
print('***********************************************\n')

# verbose is a global variable, which is convenient here, but generally
# a bad practice.

verbose = False

# Following 2 lines are required work-around to use IDLE
##sys.argv = [sys.argv[0],'-v','-a','segments','inpath','outpath']
#sys.argv = [sys.argv[0],'-v', '-a'] 
print ('sys.argv = ', sys.argv)

def vprint(obj):
	'Prinnt if verbose is True.'
	if verbose: print(obj)

def listprint(lst):
	for item in lst: print(item)

def washme(filename):
    ''' Take a file name, possibly with blanks and "-" then
    return washed_name without blanks and minus signs (hyphens).
    All of "wash" could be done in one line as list comprehension.
    It would be more "Pythonic" and IMHO harder to read.
    The statment "harder to read is" hotly disputed, hence IMHO.
    Well, this is a more "Pythonic" version. If you can read it and
    comprehend, you deserve a masters!'''
    
    w = ''
    for x in [v+'_' for v in filename.replace('-',' ').split()]:
        w += x
    return w[:-1]

def logit(data_dir):
    '''In the cute folder, data processing is in 3 stages:
"fresh_data" is a directory with freshly imported data - nothing is ever
written to fresh_data, other than importation of a bunch of files.
"data"  has the files, partly processed, viz changed file names
"output" has the files written by Handbrake. It also has the logbook.'''
    w = ''
    lst = os.listdir(data_dir)
    lst.sort()
    for v in lst:
        w += v + '\n'
    return w
# 
# program is usefull for multi media file organisation to ease access
# to available media files and to transcode file when transcoding
# facilitates access.


def prolog():
    'Initialise arguments for execution of the program.'
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose',action='store_true',
                        help='Verbose output to help debugging.')
    parser.add_argument('-a','--allow',action='store_true',
                        help='Allow modification of data on disk.')

    parser.add_argument('segments',nargs='?',default=[],
    help='segs[0] ch at start, segs[1] at end makeup the file name.')
    parser.add_argument('inpath',nargs='?',default=os.getcwd()+'/data/',
           help='absolute path to data directory.')
    parser.add_argument('outpath',nargs='?',default=os.getcwd()+'/output/',
                        help='absolute pathe to output directory.')

    args = parser.parse_args()
    if args.verbose:
        print('prolog finished setting up of args.')               
        print('Name space args = ', args)
    verbose = args.verbose          
    return args

def one():
	return

def fix_filenames(args):
    ''' The old file name or its segments makes up the new name. 
Once the new names are made, all blanks in the name are replaced 
by underscore. Contiguous blanks are replaced by one undersore. 
File name extensions, indicating the type of file, are kept.'''
    verbose  = args.verbose
    allow    = args.allow
    segments = args.segments
    inpath   = args.inpath
    outpath  = args.outpath
    vprint('***fix_filenames***')
    print('\n Formatted Namespace args = \n','verbose = ', verbose,'\n',
          'allow = ',allow,'\n','segments = ',segments,'\n',
          'inpath = ',inpath,'\n','outpath = ',outpath,'\n')
    # the parameters (paras) will need to be read by this program as data
##    videos = 'This is the list of the content of the videos.'
    videos = logit('fresh_data')
    print('videos','\n' + videos)
    with open('output/video_list','w') as f1: f1.write(videos)
    shortnames = []
    vprint('fresh_data:')
    filenames = os.listdir('fresh_data')
    print('debug * information: segments = ', segments)
    if len(segments) == 0:
        for filename in filenames:
            shortname = washme(filename)
            shortnames.append(shortname)
        shortnames.sort()
        listprint(shortnames)
    else:
#  This section is bubby and requires heavy editing				
#  This section is bubby and requires heavy editing				
        for filename in filenames:
            w_filename = washme(filename)
            print(w_filename)
            shortname = w_filename[:segments[0]] + w_filename[segments[1]:]
        shortnames.append(shortname)
        shortnames.sort()
    print('verify list of shortnames')
    listprint(shortnames)
    for i in range(len(filenames)):
        shutil.copy('fresh_data/'+filenames[i], 'data/'+shortnames[i]) 
    print("Finished up filenames.")   
    return

def transcode(args):
    print('I am transcode(args)')
    cwd = os.getcwd() 
    print('cwd = ', cwd)
    filenames = os.listdir(cwd + '/data/')
    filenames.sort()
    listinput = []
    
    for name in filenames:
        start_time = time.time()
# Theis needs to be more general = more than name.flv or .avi
        if name[-4: ] == '.avi':
            listinput.append(name)
            subprocess.call(["HandBrakeCLI", "-i",cwd + '/data/'+ name,
                            "-o", cwd + '/output/' + name + '.mp4'])
        
        print('processed = ', name + '.mp4')
        arrival_time = time.time()
        print('Elapsed time for file transcode = ',
              int(arrival_time - start_time),' in seconds.')
        print('Transcode loop completed\n')
    print('filenames = ', filenames)
    return

def main():
    print('main program accessed')
    args = prolog()
    if args.verbose:
        print('Show args in the main = ', args)
    fix_filenames(args)
    if args.allow:
        transcode(args)
    return

if __name__=='__main__':
    main()

## todo:
## Do some testing as a finished program, i.e. no temporary 'easy' 
## corrections. Last stage in 2015!
