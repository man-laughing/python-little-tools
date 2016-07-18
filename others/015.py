#!/usr/bin/python
import os,sys,time
self = sys.argv[0]
filename = time.strftime('%Y-%m-%d-%H%M') + '.'+'tar.gz'
print '''\033[033m
-----------Start Backup Program--------------------
\033[0m''' 
try:
    source = sys.argv[1]
    dest   = sys.argv[2]
    new_dest = dest + filename
    command = 'tar zcf %s %s' % (new_dest,source)
    if os.system(command) == 0:
        print 'Backup success.'
    else:
        print 'Backup faied.'
except IndexError:
    print 'Usage: %s SOURCE_FILE  DESTINATION_PATH' % self
