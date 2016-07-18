#!/usr/bin/python

fab = [0,1]
def abc():
    fab.append(fab[-1] + fab[-2])
    print fab

for i in range(10):
    abc()
