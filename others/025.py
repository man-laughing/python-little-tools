#!/usr/bin/env python

import socket

host = '192.168.124.128'
port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
conn,addr = s.accept()

while True:
    data = conn.recv(1024)
    print data
    if not data:break
    conn.sendall(data)
conn.close()
