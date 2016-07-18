#!/usr/bin/python

import pickle

account_info = {
    '123456': ['alex3714',15000,15000],
    '654321': ['wode',2000,2000]
}

f = open('acc.pkl','w+')

pickle.dump(account_info,f)
f.close()
