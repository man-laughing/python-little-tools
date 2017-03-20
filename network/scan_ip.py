#!/usr/bin/env python

import sys
import Queue
import commands
import threading

def checkPara():
    try:
        bool(sys.argv[1])
    except IndexError:
        print
        print "Usage: " + sys.argv[0] + " networkId"
        print
        print "Example: " + sys.argv[0] + '.' + " 10.10.10."
        print 
        sys.exit()

def makeData():
    user_input = sys.argv[1].strip()
    q1 = Queue.Queue()
    for i in xrange(1,256):
        if user_input.count('.') == 2:
            ip = user_input + '.' + str(i)
            q1.put(ip)
        else:
            ip = user_input + str(i)
            q1.put(ip)
    return q1
    
def gorun(queueObj):
    while 666:
        realip = queueObj.get()
        comm = commands.getstatusoutput("ping -c 1 -W 1 " + realip )
        if comm[0] == 0:
            print "%s is online"  % realip
        queueObj.task_done()
         
if __name__ == "__main__":
    checkPara()
    z = makeData()
    for i in range(100):
        run1 = threading.Thread(target=gorun,args=(z,))
        run1.setDaemon(True)
        run1.start()  
    z.join()
