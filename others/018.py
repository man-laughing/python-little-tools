#!/usr/bin/python

try:
    #raise NameError
    abc = 'zhanglei'
    print abc
except NameError:
    print "The variable is not found."
else:
    print "Thank you"
finally:
    print 'hello,world'
