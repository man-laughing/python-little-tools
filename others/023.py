#/usr/bin/python

class human():
    def __init__(self,guoji):
        self.country = guoji
    def info(self,name,age):
        print 'Name is %s,Age is %s,Country is %s.' %(name,age,self.country)

zl = human('CN')
zl.info('zhanglei',22)


