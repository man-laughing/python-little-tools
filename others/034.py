#!/usr/bin/python

import paramiko
#information = ['221.203.142.36',34729,'mon','mon_Ps@)!%09']
information = ['180.97.75.5',27945,'zhanglei','yiyunzhanglei']
ip,port,user,passwd = information

mytest = paramiko.SSHClient()
mytest.set_missing_host_key_policy(paramiko.AutoAddPolicy())
mytest.connect(ip,port,user,passwd)
stdin,stdout,stderr = mytest.exec_command("echo hello")
#print stdout.readlines(),stderr.readlines()
print stdout.readlines(),stderr.readlines()
mytest.close()

