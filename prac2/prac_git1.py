'''
Created on 26 May 2018

@author: laxminarayan rao
'''

#import os 
x = raw_input('enter name of the file  :')
f = open(x,'w')
print 'enter data in to file:',x

while True :
    data = raw_input()
    if data in 'Qq' : break
    f.write(data)
    f.write('\n')

f.close()


import os
xsx = raw_input('enter the file name :')
    if os.path.exists(xsx) :
        if os.path.isfile(xsx) :
            st =raw_input('enter the string to delete')
            with open(xsx,r) as x:
               d1=  x.read() # read returns in string format !!
               d2=  x.replace(st,'')
             print  d2 
        else :
            print xsx,'is not a file'
    else :
        print xsx,'no such file or directory'

