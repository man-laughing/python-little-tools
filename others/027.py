#!/usr/bin/env python

import socket
from time import sleep

host = '192.168.124.128'
port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall('hello,MR.Lilei')
data = s.recv(1024)
print 'Reveived',repr(data)
s.close()
