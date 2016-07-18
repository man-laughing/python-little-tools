#!/usr/bin/env python

class person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        print name
        print age
    def wocao(self):
        print self.name
        print self.age
#    def sayHI(self):
#        print 'Hello,Your name is %s and you age is %s.' %(self.name,self.age)

zl = person('zhanglei',22)
zl.wocao()

