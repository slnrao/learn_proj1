'''
Created on 9 Apr 2018

@author: laxminarayan rao
'''
'''x=['sdrao','ssrao','cbrao','csrao','chrao','charshi']
y=[999,888,777,666,555,444,333]

n= x.index('cbrao')
print n
#print y(n)# TypeError: 'list' object is not callable
print y[n]# use []
'''
# Dictionary elements are always enclosed in flower brases {}
'''
d1 = {'sdrao':'ssrao','csrao':'cbrao','thata':'amma','pkrao':'aruna','bala':'suma'}
print d1['csrao']# calling elements in \dictionary 
print len(d1)
d1['bajirao']='masthani'# adding elements to dictionary 
d1['ranu']='swapna'
print d1
print len(d1)
print d1['bala']
print d1['bajirao']
d1['bajirao']='rakshasi'# if element exist it will over write 
print d1['bajirao']
del d1['ranu']# to delete the element from dictionary 
print d1
print len(d1)
print d1.has_key('bajirao')# has_key method id used to check wheather the key exists or not !!
if d1.has_key('manoj') :# if statement should be wrapped in () not in []
    pass
else :
    d1['manoj'] ='swathi'
print d1

# if d1.has_key('bajirao') :
#     pass
# else :
#     d1['bajirao']='bujji'
# print d1
#  
# if d1.has_key('bajirao') : # this dosn't works !!
#     False
# else :
#     d1['bajirao']='bujji'
# print d1

print d1.keys() # this returns all the keys !!
print d1.values() # this returns all the values !!
print d1.items() # this returns key values in tupple format !!

for i in d1.keys() :
    print i,"partner is : ", d1[i]# i iterates keys()with d1[i]
      
for i,j in d1.items() :
    print i,"is married to :",j # since items has( key,values ) it takes 2 values i & j !!

A = d1.copy()
print A
print A.items()'''

'''
dx= {'sdrao': 'ssrao', 'bajirao': 'rakshasi', 'thata': 'amma', 'bala': 'suma', 'pkrao': 'aruna', 'csrao': 'cbrao', 'manoj': 'swathi'}
print dx 
print type(dx)

y={9:101,8:202,7:303,6:404,5:505}
y.update(dx) # this appends dict dx
print y 

print dx

print dx.has_key('thata')
print dx.has_key(5) #its call by reference and call by value  !! y and dx address are same but memory is different !!

print y.has_key(4)
print y.has_key(8)

y.clear() # this returns just empty dict {}
print y 
'''
# del y # NameError: name 'y' is not defined
# print y

'''a1 = {1:101,2:201,3:301}
print a1
b1 = a1 #call by reference !!
print b1

a1[2]=222
print a1
print b1
del b1[3]
print b1 
print a1 # all above effect is because of "call by reference "

v1 = {4:104,5:105,6:106,7:107}
v2 =v1.copy() #call by value !!
print v1 
print v2

v1[6]=666
print v1
print v2# no values get changed because v2 is created by "call by value "
'''

# DICTIONALRY COMPRIHENSHION 
'''
g= {i : i * i for i in range(1,101)}
print g

print g[25]
print g[99]


h = {i : i*3 for i in range(2,25)}
print h
print h[8]
print h[10]


y = {i : i * 2 for i in range(1,50) if i%2==0 }
print y

w= {i : (i * i)* 5 for i in range(1,8) if i%3==1}
print w

'''
# # # # # #  Dictionary of lists # # # # # # # #
'''
dl = {'sdrao' : [101,'president',35000],
       'shobarao' : [202,'chairmain',49000],
       'cbrao' : [303,'executive',59000],
       'csrao' : [404,'cfo',9850],
       }
print dl

print len(dl)
print dl['shobarao']
print dl['cbrao']
'''
'''
------------------------------$$$$$$----------------------------------------
if dl.has_key('rishikarao') :
    pass
else :
    dl= {'rishika' : [505,'mydarling',89500]}
'''
'''
dl['rishika'] = [505,'mydarling',89500] 
print len(dl)
print  dl

print dl['rishika']
print dl.values()
'''
'''
-----------------------------------------------------------------------------------
dl2 ={'sdrao' : [101,'president',35000],
       'shobarao' : [202,'chairmain',49000],
       'cbrao' : [303,'executive',59000],
       'csrao' : [404,'cfo',9850],
       'rishika': [505, 'mydarling', 89500]
       }
print dl2
print len(dl2)
print dl2['shobarao'][1]
 
 
dlx ={'sdrao' : [101,'president',35000],
       'shobarao' : [202,'chairmain',49000],
       'cbrao' : [303,'executive',59000],
       'csrao' : [404,'cfo',9850],
       'rishika': [505, 'mydarling', 89500],
       'harshi' : [707, 'cheekymonkey','cutie',99]
       }
print dlx
print len(dlx)
print dlx['harshi'][2]
print dlx.has_key('harshi')
 
dlx['bujji'] = [907,'loveofbaji',99999] # adding elements to dictionary 
dlx['baji'] = [709,'loveofbujji',77777]
       
print dlx
print len(dlx)
 
 
print dlx.keys()
print dlx.values()
print dlx.items()
print type(dlx.items())
 
dlx['harshi'][-1] = 999999 # modify values of given !!
print dlx['harshi']
-----------------------------------------------------------------------------------
'''
'''
-------------------------------------------------------------------------------------------

# Dictionary with in a dictionary  !!

dd = {'bala' : {'eid':109,'job':'director','sal':320000},
      'suma' : {'eid':209,'job':'chairperson','sal':250000},
      'bhoomi' : {'eid':309,'job':'schoolgirl','sal':'allbonous'},
      'nithin' :{'eid':409,'job':'cadcam','sal': 95000},
      }
print dd
print len(dd)
print dd['nithin']

dd['slaro'] = {'eid':509,'job':'H1B','sal':125000}
dd['prathick'] ={'edi':609,'job':'H1B','sal': 95000}
print dd['slaro'].keys()
print dd['slaro'].values()
print dd['prathick'].items()

print len(dd)
print dd.keys()
print dd.values()
print dd.items()

print dd['bhoomi'] # dictionary in dictionary maniplation !!
dd['bhoomi'][-1]= 890000
print dd['bhoomi']
dd['bhoomi']['sal'] = 890000
print dd['bhoomi']

del dd['bhoomi'][-1]
print dd['bhoomi']

for i in dd.keys() : # to find keys in a big file in real time 
    print i
    
for a in dd.values() : # to find values in a given file o dictionary  
    print a
    
for l,j in dd.items() : # to find key and values in a given file 
    print l,'',j

----------------------------------------------------------------------------------
'''
'''
a = {1:'z',2:'x',3:'y'}
print dir(a)

print help(a.items)
# print help(a.count)
# print type(a.count)
'''
'''
--------------------------------------------------------------------
#Adding elements(key,values) to dictionary at run time  !!!
courses = {}
while True :
    cname =raw_input('Enter course name [to stop press "q"] :')
    if cname in "Qq" : 
        break 
    fee = input('Enter course fee :')
    courses[cname]=fee
print "Coureses Details ......."
for i,j in courses.items() :
    print i,':',j 

-----------------------------------------------------------------------
'''

#Assignment WAS using dictionary of items and its prices  !!

x = {}
while True :
    pname = raw_input("Enter product name [press ' q ' to stop ] :")
    if pname in 'Qq' : break 
    price = float(input('Enter the price :'))
    x[pname]=price 
  
for i,j in x.items() :
    print i,':',j   
print x







    