#!/usr/bin/python
import multiprocessing 
import sys,os,time

result = []
def run(h):
    print 'Threading test is:',h,os.getpid()
    time.sleep(2)
p = multiprocessing.Pool(processes=20)
for i in range(100):
    result.append(p.apply_async(run,('%s'%i,)))
p.close()
for ii in result:
    ii.get(timeout=5)
