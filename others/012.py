#!/usr/bin/python

import re

p = re.compile('\d+')

m = p.split('one1,two2,three3,four')

print m
