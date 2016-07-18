#!/usr/bin/python
while True:
    input = raw_input('Please input your username: ')
    if input == 'laughing':
        p = int(123)
        while True:
            password = int(raw_input('Please input your password:'))
            if password == p:
                print "Welcome to login in %s" % input


                while True:
                    query_input = raw_input('PLEASE INPUT QUERY ITEM:')
                    f = file('/tmp/test')
                    while True:
                        line = f.readline()
                        if len(line) == 0:break
                        if query_input in line:print "Match ITEM:  %s" % line
                f.close()

            else:
                continue
#                print "Wrong password,try again." 
        break
    else:
        continue
#        print "Sorry, %s is not found" % input
