#!/usr/bin/env python

ipaddr = ["192.168.1.1","192.168.1.2","192.168.1.3"]
ip_dic = {}
number = 0
for i in ipaddr:
    number += 1
    ip_dic[number] = i
    print i 
print '*'*30


for k,v in ip_dic.items():
    print "\033[32m %s %s \033[0m" %(k,v)
