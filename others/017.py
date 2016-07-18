#!/usr/bin/python
#coding:utf-8
import os,time,sys,urllib
i = 1
list1 = []

source_url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
str = urllib.urlopen(source_url).read()

title = str.find(r'<a title=')
href = str.find(r'href=',title)
html = str.find(r'.html',href)
url = str[href + 6:html +5]
print url
while title != -1 and href != -1 and html != -1 and i < 50:
    title = str.find(r'<a title=',html)
    href = str.find(r'href=',title)
    html = str.find(r'.html',href)
    url = str[href +6:html +5]
    #print url
    list1.append(url)
    #print list1
    i += 1
for i in list1:
    print i
