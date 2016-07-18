#!/usr/bin/env python

from __future__ import division
import socket
import os
import time

class collect:
    def flux(self):
        with open('/sys/class/net/eth0/statistics/rx_bytes','r') as f:
            ff = f.read()
            ff_int = int(ff)
        time.sleep(1)
        with open('/sys/class/net/eth0/statistics/rx_bytes','r') as b:
            bb = b.read()
            bb_int = int(bb)
        test  = bb_int - ff_int
        result = test * 8  /1024 /1024
        result_str = str("%.2f"%result)
        return result_str

    

address = ('192.168.124.128',18000)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(address)
while 1:
    abc = collect()
    cccc = abc.flux()
    s.send(cccc)
    print "Send data is",cccc
s.close()

