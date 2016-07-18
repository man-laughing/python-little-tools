#!/usr/bin/env python
import socket
host = '192.168.124.128'
port = 18000
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect((host,port))
ss.send('hi,friend')
ss.close()
