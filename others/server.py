#!/usr/bin/env python
import socket
import sys
import MySQLdb

conn = MySQLdb.connect (
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'excloud8',
    db = 'test'
)
cur = conn.cursor()
conn.select_db('test')

host = '192.168.124.128'
port = 18000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(65535)
while 1:
    conn,addr = s.accept()
    while 2:
        data = conn.recv(1024)
        if data == "":
            sys.exit(1)
        print "You are from",addr,"data is",data
        sql = "insert into ttt values (%s)" %data
        cur.execute(sql)
cur.close()
conn.close()
s.close()
