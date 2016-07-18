#!/usr/bin/env python

from multiprocessing import Process,Lock
import time,os

def sayhi(i):
    print 'hello,world',i
    time.sleep(10)
#lock = Lock()
for n in range(100):
    p = Process(target=sayhi,args=(n,))
    p.start()
    #p.join()

