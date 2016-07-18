#!/usr/bin/env python
#coding:utf-8
import sys
import urllib

old_url = '<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'
title = old_url.find('a title')
#print title
href = old_url.find('href')
#print href
html = old_url.find('.html')
#print html
new_url = old_url[href + 6:html +5]
print new_url

content = urllib.urlopen(new_url).read()
f = open('zl.txt','w')
f.write(content)
f.close()
