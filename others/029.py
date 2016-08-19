#!/usr/bin/env python

import smtplib

mail_server = 'smtp.qq.com'
user = '305835227'
password = 'yourpasswd'
from_addr = '305835227@qq.com'
to_addr   = 'zhanglei@exclouds.com'
msg       = '''
 From:    zhanglei<305835227@qq.com>
 Subject: Have Dinner?
 Message: Hello,MR.Zhang.I want to have a dinner with you?
          Do you have free time?
'''
smtpobject = smtplib.SMTP(mail_server)
smtpobject.login(user,password)
smtpobject.sendmail(from_addr,to_addr,msg)
