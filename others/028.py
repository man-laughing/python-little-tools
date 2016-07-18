#!/usr/bin/env python

import ftplib
 
ftp = ftplib.FTP()
ftp.set_debuglevel(2)
ftp.connect('192.168.124.128')
ftp.login()
print ftp.getwelcome()
ftp.cwd('nide')
ftp.dir()

bufsize = 1024
filename = 'nide'
file_handler = open(filename,'wb').write
ftp.retrbinary('RETR nide',file_handler,bufsize)
ftp.set_debuglevel(0)

ftp.quit()
