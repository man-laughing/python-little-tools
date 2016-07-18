#!/usr/bin/env python

import socket
from time import sleep

host = '192.168.124.128'
port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    s.sendall('hello,MR.Zhang.')
    data = s.recv(1024)
    sleep(1)
    print 'Reveived',repr(data)
s.close()
