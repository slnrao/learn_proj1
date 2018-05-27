'''
Created on 11 Apr 2018

@author: laxminarayan rao
'''
# print is a key word in python 2 and function in python 3

'''print "slrao",
print "bujji" 

print " slrao ", # must be in "" and fallowed by , 
print "loves",
print "bujji",
print "loves",
print "bajji"
'''



# for python 3
# print("slrao", end =': ')
# print("bujji")

#indexing and slicing string and a int 
'''
x= 'hadoopisacombinationofstorageandprocessing'
print  x
print  x[0:6]+' '+x[6:] # slice and concatenate using ' + ' operator !!
print  x[0:6]+' '+x[6:8]+' '+x[8]+' '+x[9:]
print  x[0:6]+' '+x[6:8]+' '+x[7:]
print  x[0:6]+' '+x[6:8]+' '+x[8:]
print  x[0:6]+' '+x[6:8]+' '+x[8]+' '+x[9:20]
print  x[0:6]+' '+x[6:8]+' '+x[8]+' '+x[9:]
print  x[0:6]+' '+x[6:8]+' '+x[8]+' '+x[9:20]+' '+x[20:22]+' '+x[23:]
print  x[0:6]+' '+x[6:8]+' '+x[8]+' '+x[9:20]+' '+x[20:22]+' '+x[22:]
print  x[0:6]+' '+x[6:8]+' '+x[8]+' '+x[9:20]+' '+x[20:22]+' '+x[22:29]+' '+x[29:]
print  x[0:6]+' '+x[6:8]+' '+x[8]+' '+x[9:20]+' '+x[20:22]+' '+x[22:29]+' '+x[29:32]+' '+x[32:]
'''

'''x = 919246578467

print str(x),type(x)
'''


# conversion of sting and number for slicing 


# range function
# in python  2.7
# range (1,5 ) # excluding  upper limit 
# range (1,10,2)# with step 2
# range (1,10,1)# with step 1
# range (15,-1,2)
# in py 3 
# list(range(1,15)) # we have to list the range and the rest is same !!


'''
8888888888888888888888888888888888888888888888888888
# Basic programs 
# raw_input and input functions !!
x= raw_input('Enter a name :')
print x
print x,type(x)
888888888888888888888888888888888888888888888888888
'''
'''
name = 'hari'
age =11
print 'hello',name,'nice to meet you and you are',age,'old'



name = raw_input('what is your name :')
age = input('enter your age :')

print 

a= input('enter number 1:')
b= input('enter number 2 :')
c= a+b
print ('sum ',c)

a= input('enter number 1:')
b= ('enter number 2 :')
c = int(a)+int(b)
print ('sum',c)
print ('a=',type(a)) #<class 'str'>
print ('b=',type(b)) #<class 'str'>



a= int(input('enter number 1 :'))
b= int(input('enter number 2 :'))
c = (a)+(b)
print ('sum :',c)
'''
'''
----------------------------------------------------------------------------------------
#WAP accepting empno,ename,sal and calcuclate bonus based on the following condition

empno =  input('Enter employee number : ')
ename =  raw_input('Enter employee name :')
esal  =  input('Enter employee salary : ')

annul_salary  =  esal*12
bonus         =  annul_salary*20/100

print '\t\t EMPLOYEE BONOUS REPORT '
print '-' * 50
print '\t Employee number : ', empno
print '\t Employee name   : ', ename
print '\t Employee salary : ', esal
print '\n\t Annual Salary : ', annul_salary 
print '\t Employee Bonus  : ', bonus 
print '-' * 50

------------------------------------------------------------------------------------------
'''

'''
# arthimatic opperators !!
# float division 
print 10/6
print 10//6


a,b,c=100,3.5,'abc' 
print (a,b,c)
print a

'''
#WAS accepting a number check the given number id even or odd number 
'''
        ----------------------------------
n = int(input('Enter a Number :'))
if n%2==0 :
    print n,' is a even number '
else :
    print n,' : is a odd number '
    

if n>10 and n<100 :
    print n,'is a 2 digit number '
else :
    print n,'is not 2 digit number '
    
if abs(n)>10 and abs(n)<100 :
    print n ,'is a +ve 2 digit number ' 
         ------------------------------
'''  
# '''WAS TO CREATE USER NAME AND PASSSWORD SET UP !!
'''
--------------------------------------------------------
username = raw_input('Enter username :')
password = raw_input('Enter password :')
# password = int(raw_input('Enter password :'))# trying to set alfa numeric password 

if   username  == 'sdrao'   and  password =='shoba007' :
    print ' '
    print '$$$ welcome to python $$$ '
else :
    print 'invalid username or password '
--------------------------------------------------------
'''   
    
'''    
if   username  == 'sdrao'   and  password =='shoba007' :
#     print ' PYTHON WELCOMES YOU '
    if   username  == 'bajirao' and  password =='bujji' :
            print ' '
            print '$$$ welcome to python $$$ '
#     print ' '
#     print ' PYTHON WELCOMES YOU '
else :
    print 'invalid username or password '
'''
 
#-------------if ,elif and else ----------------

# 04/16/18
#looping controll statements :

#WAS accepting a string and count the length of the string with out  using len function 




x = 'laxmi'
print x.ljust(10,'*')


print x.rjust(10,'#')

print x.ljust(10,'#').rjust(12,'!')

print x.ljust(12,'#').rjust(17,'!')

print x.rjust(10,'#').ljust(12,'!')

# 



