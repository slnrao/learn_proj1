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
