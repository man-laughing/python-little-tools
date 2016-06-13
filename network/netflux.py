#!/usr/bin/env python
#Author: laughing
#Mail:   305835227@qq.com
#Description: This script can help you view your network bandwidth

from __future__ import division
import sys,time

def usage():
    print ""
    print "Usage:",sys.argv[0],"[eth0|eth1|eth2]"
    print "Example:",sys.argv[0],"eth0"
    print ""
try:
    one = sys.argv[1]
    aa = '/sys/class/net/'
    rxx = '/statistics/rx_bytes'
    txx = '/statistics/tx_bytes'
    rx = aa + one + rxx
    tx = aa + one + txx
    empty = " " * 10 

    def flux():
        with open(rx,'r')as r:
            rr = r.read()
            rr_int = int(rr)
        with open(tx,'r')as t:
            tt = t.read()
            tt_int = int(tt)
        time.sleep(1)
        with open(rx,'r')as f: 
            rrr = f.read()
            rrr_int = int(rrr)
        with open(tx,'r')as abc:
            ttt = abc.read()
            ttt_int = int(ttt)
        r_flux = (rrr_int - rr_int) /1024 /1024 * 8
        t_flux = (ttt_int - tt_int) /1024 /1024 * 8
        mytime = time.ctime().split()[3]
        print mytime,"Input:","%.2lf" % r_flux,"MB/bps",empty,"Output:","%.2lf" % t_flux,"MB/bps"
    while True:
        flux()
except IndexError:
    usage()
