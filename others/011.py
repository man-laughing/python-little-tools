#!/usr/bin/python

import re
 
p = re.compile('hello')

m = p.match('hello,world')

print m.group()
