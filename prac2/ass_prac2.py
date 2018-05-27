'''
Created on 17 Apr 2018

@author: laxminarayan rao
'''
# 4) WAS accepting a string and a character and count how many time times given character is appeared 
from lib2to3.fixes import fix_raw_input
from itertools import count
from _bsddb import DB_FCNTL_LOCKING
'''st = raw_input('Enter a string : ')
ch = raw_input('Enter a character :')
count = 0
for i in st :
    if i in ch :
        count = count+1
print ch,'occured in given string is',count '''

#1) WAS accept a string and find the length of a string with out using len() function :

'''st = raw_input('enter a string :')
count = 0
for i in st :
    count = count +1
print 'length of  given string is :',count'''

#2)write a script and accept a string and count number of vowels in that string :

'''st1 = raw_input('Enter the string :')
cnt =0 # a=e=i=o=u=0 CANT APPLY THIS LOGIC HERE 
for x in st1 : 
    if x in 'aeiouAEIOU' :
        cnt+=1
print 'total vowels in the given string -',st1 ,'-is : ',cnt '''

#3) write a script accept a sting and count each vowel in that string !!!

'''
st = raw_input('Enter a string :') 
a=e=i=o=u=0

for x in  st :
    
    if      x   in  'aA'    : a =a+1 #a+=1
    elif    x   in  'eE'    : e+=1
    elif    x   in  'iI'    : i+=1
    elif    x   in  'oO'    : o+=1
    elif    x   in  'uU'    : u+=1
    
print "Total no of a's in given string",a
print "Total no of e's in given string",e
print "Total no of i's in given string",i
print "Total no of o's in given string",o
print "Total no of u's in given string",u

print "Total no of VOWELS in a ",st,'string is:',a+e+i+o+u
'''
#5)WAS accepting a string and reverse the string :
'''
st = raw_input('enter a string :')
x= st[::-1] #use [::-1] to reverse a string !!
print x  
y = x[::-1] # re  reveres to original string !!
print y
'''
#6) WAS accepting a string and a character and removing that character from  that string !!
'''
st = raw_input('Enter a string :')
ch =raw_input('enter character to be removed from string :')
temp = ' '
for i in st :
    if i!= ch : # 
        temp = temp+i
print temp

'''

'''st = raw_input('Enter a string :')
ch =raw_input('enter character to be replace with :')
#temp = ' '
for i in st :
    if i in ch :
        i.replace('+','') # 
       # temp = temp+i 
#print temp
print i       
'''
#7)WAS accept a string remove vowels in a string 

'''st = raw_input('Enter a string :')
ch = raw_input('enter vowels :')
count = 0
for x in st :
    if x!= ch :
        count = count + x
print count
 '''
#8)

#9) WAS accept  print even numbers from 1 to 100
   
'''$$ this script is not right !!
num = input('enter the numbers :')

for i in range(1,101) :
    if i%2==0:
        
print i
'''

'''
import os

f = raw_input('Enter the file name :')
if  os.path.exists(f) :
    if os.path.isfile(f) :
        str1 = raw_input('enter the string to delete :')
        with open (f,'r') as x :
            data = x.read()# read returns in string format !!
            data1= data.replace(str1,'')
            print data1
            
    else :
        print f ,'is not a file !'
else :
    print f ,'no such file or directory'
 '''           
#  from assenments if the words dont found and if the word found   
'''
import os
fi = raw_input('Enter the file name :')
if os.path.exists(fi) :
    if os.path.isfile(fi) :
        st = raw_input('enter the string:')
        with open (fi,'r') as x :
            data = x.read()
            d1 = data.find(st)
        if d1>=0 :
            print data[d1:]
        else :
            print st,'word not found in the file !!'
    else :
        print fi,'file dont exits !!'
else :
    print fi,'no such file or directory !!'
'''
    
# write a script to delete all empty lines in a given file 

import os
f2 = raw_input('enter the file name :')
if os.path.exists(f2) :
    if os.path.isfile(f2) :
        with open (f2,'r') as x :
            fx= x.readlines()
            print fx
            cnt = fx.count('\n')
            print cnt  # \n will count empty lines
            if cnt >0 :
                temp =''
                for i in fx :
                    if i!='\n' :
                        temp = temp + i
                with open (f2,'w') as x :
                    x.write(temp)
                    print 'all the empty lines are deleted from',f2,'file'
            else :
                print 'there are no empty lines in the file',f2
    else :
        print f2,'is not a file !!'
else :
    print f2,'is not a file or directory'






















