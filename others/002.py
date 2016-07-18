#!/usr/bin/python
product = ['Car','Iphone','MAC','Coffee']
price   = [100000,4599,10000,35]
shop_list = []

while True:
    input = int(raw_input("Please input your money: "))
    print "Your money is: %s" % input
    for i in product:
        product_index = product.index(i)
        print i,'is',price[product_index]
    choice = raw_input("Please input one item to buy: ")
    if choice in product:
        choice_number  = product.index(choice)
        choice_prices  = price[choice_number]
        if input > int(choice_prices):
            print "You buy it."
        else:
            print "Sorry,you don't have enough money."
    else:
        print "Sorry,we have't this product."
