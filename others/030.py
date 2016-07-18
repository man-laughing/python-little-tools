#!/usr/bin/env python
import MySQLdb
e = 'fucking dog'
try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='excloud8',port=3306)
    cur = conn.cursor()
    conn.select_db('mysql')  #cd the mysql database.
    cur.execute('select User,Host from user')
    result = cur.fetchall()  #collect all data to result.
#    result = cur.fetchone() #collect first data to result.
    for i in result:
        print i
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print 'MySQL Error MsG:',e
