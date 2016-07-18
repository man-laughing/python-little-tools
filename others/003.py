#!/usr/bin/python
f = file('abc')
products = []
prices = []
for line in f.readlines():
    new_line = line.split()
    products.append(new_line[0])
    prices.append(new_line[1])
print products
print prices
