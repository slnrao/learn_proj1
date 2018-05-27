'''
Created on 14 Apr 2018

@author: laxminarayan rao
'''

'''
x= open('a1.doc','w')
x.write('this file is i schech how the data \n')
x.write('appended when we run the same script \n')
x.write('and to create duplicates \n')
x.write('so i can practice how to elemeinate duplicates from agiven record ')
x.close()
print x
'''

'''
------------------------------------

f1 =open('filehandeling1.txt','w')
f1.write('python is simple' )
f1.write('it is easy to learn')
f1.write('python is a scripting language' )
f1.write('python needs lot of practice' )
f1.close()
print f1, 'is created'

--------------------------------------
'''
'''
--------------------------------------
f1 =open('filehandeling1.txt','w')
f1.write('python is simple \n' )
f1.write('it is easy to learn \n')
f1.write('python is a scripting language \n' )
f1.write('python needs lot of practice' )
f1.close()
print f1, 'is created'
-----------------------------------------
'''
'''
------------------------------------------
f2 =raw_input('Enter The File Name  :')
f= open(f2,'w')
f.write('files handeling is very importent in python  \n')
f.write('in real time file handeling is every thing \n')
f.write('we can create all foramts of files like text , json, csv etc')
f.close()
print f2 ,'is successfully created !'
-------------------------------------------
'''

'''
----------------------------------------------
f2 =raw_input('Enter the File Name  :')
f= open(f2,'a')
f.write('this is  to appending \n')
f.write('by opening file with mode as "a" \n')
f.write('files handlling is very important in python  \n')
f.write('in real time file handlling is every thing \n')
f.write('we can create all formats of files like text , json, csv etc')
f.close()
print f2 ,'is successfully created !'
----------------------------------------------
'''
'''
----------------------------------------------
nf = raw_input('Enter New File Name :')
f = open(nf,'w')
print 'Enter input data in to new file :'
data=raw_input()
f.write(data)
f.close()
print nf,' is successfully created : '
----------------------------------------------
'''
'''
-----------------------------------------------

f3 = raw_input('Enter Name of the file :')
x  = open(f3,'w')
print 'Enter INput Data in to file [press q to exit] :'
while True : # since raw_input can only write 1 line if data , so use while loop 
    data = raw_input() 
    if data in 'Qq' : break 
    x.write(data)
    x.write('\n')
x.close()
print f3,'is successfully created'
-------------------------------------------------
'''

'''
-------------------------------------------------
nf = raw_input('Enter New File Name :')
f = open(nf,'w')
print 'Enter input data in to new file :'
data=raw_input()
f.write(data)
f.close()
print nf,':is successfully created !! '
-------------------------------------------------
'''
'''
------------------------------------------------
a = open('C:\Users\laxminarayan rao\Desktop\sowjilaxminarayan rao (2)','r')
x = a.read()
print x
print type(x)
------------------------------------------------
'''
'''
b = open('C:\Users\laxminarayan rao\Desktop\projectpython\FH2_creating_at_runtime','r')
c = b.read()
print c
print len(c)
print type(c)


x = b.readlines()
print x
print len(x)
print type(x)


for i in x :
    print i 
    
for i in x[::-1] : # to read in reverse  in order 
    print i
    
for i in x[::2] : # to read alternate lines in the file
    print i 
    
print len(x)
print type(x)
x = set(x)
print type(x)
print len(x)
# print (x)
x = list(set(x))   
x = ' '.join(x)  
print x
print len(x)
print type(x)  #!!'IM GETTING A DUBLICATE RECORD AFTER CONVERING IN TO SET ' !!
'''
'''
fn = raw_input('Enter the file name :')
string = raw_input('Enter the string to be deleted:')
x = open(fn,'r')
k = x.read()
k = x.replace(string,'')
x.close()
print string,'- is deleted  from the file',fn
print ' ********** file after deleting ',string,'from the given file ********* '
print k 
'''
'''
---------------------------------
x = open(r'C:\Users\laxminarayan rao\eclipse-workspace\IF&Elif\prac2\a1','r+')
x.write('******* try to open a file and write inn \n')
x.write('hope this appends ')
print x
x.close()
---------------------------------
'''
'''
---------------------------------
a = open(r'C:\Users\laxminarayan rao\eclipse-workspace\IF&Elif\prac2\a1','r+')
a.write('this to check again how data  can be appended in exixting file \n')
a.write('lets check this  will gert apppended in the abovefile ')
a.close() # since this is opened in r+ mode which is read and write text mode , the file is wiped off and writan the above 2 lines in the existing lines  
---------------------------------
'''

'''
b = open(r'C:\Users\laxminarayan rao\eclipse-workspace\IF&Elif\prac2\a1','w+')
b.write('this is to add data to the exist file \n')
b.write('from above set of code , these 2 lines should get appendded to the file called "a1"\n')
b.close()
'''
'''
c = open(r'C:\Users\laxminarayan rao\eclipse-workspace\IF&Elif\prac2\a1','a+')
c.write('this is opened in a+ mode so it should be get appended \n ')
c.write('there should be two lines above this to lines i,e all together now 4 lines of data in the file \n')
c.close() # this 1 is working well !!! if i need to append any data in the existing the file should be opened in a+ mode and its keep get appended as many time we run the script
'''


'''#########################################
x = open('a1','a+')

# f = x.read()
# print f
# print type(f) 
y =x.readlines()
for i in y :
    i.replace('this','--')
    y.write('i')
    
print y
y= 'a1'
x.close()
#############################################'''

'''$$$$$$$$$$$$$$$ accept a file and count number of lines , characters and the total words in the file !!
fn = raw_input('Enter a filename :') # paste this file C:\Users\laxminarayan rao\Desktop\python bysridavi\projectpython\file_data@runtime
x = open(fn,'r')
a = x.readlines()
lcnt = len(a) # this gives the  number of lines 
print len(a)

x.seek(0,2)
cc = x.tell() # gives the total 
print cc

wc = 0 # word count
for i in a :
    words = i.split(' ')
    wc=wc+len(words)
print wc

x.close()
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
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    









