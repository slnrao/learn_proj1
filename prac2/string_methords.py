'''
Created on 12 Apr 2018

@author: laxminarayan rao
'''

'''
------------------------------------------------------------------------
x="hello"
print x.upper() # UPPER AND LOWER FUNCTIONS  IN STERING METHORDS 
print x 

y = 'devender rao'
print y.upper()

print y.lower()=="devender rao" #TRUE
print y=="DEVENDER RAO"#FALS

a="laxmiNARAYAN rAo"
print a.swapcase() # lower to upper and upper to lower is called SWAPCASE!!

u = 'python is simple and easy to learn '
print u.title()#it CHANGES FIRST LETTER  of every word in top UPPERCASE !!
print u.capitalize() # CAHNGES FIRST LETTER OF THE SENTENCE IN TO UPPER CASE !!
print u.count('easy')
print u.count('hard')
print u.count("python")

q = '  laxminarayan rao s  '
print q.lstrip()#deletes left most spaces 
print q.rstrip()#deletes right most spaces 
print q.strip()#deletes  both left and t=right most spaces 

st = 'tecnosoft'
print st.lstrip()#tecnosoft
print st.lstrip('t')#ecnosoft
print st.lstrip('p')#tecnosoft

print st.rstrip('t')#

print st.strip('t') #

s1 = 'tecnosoft1'
print s1.rstrip()#

print s1.strip('t')

w = 'hello python python is simple python is easy'
print w.count('python')
print w.count('script')
print w.count('PYTHON')# its a case sensitive !!

print w.find('python')
print w.find('python',7)
print w.find('python',14)
print w.find('python',10,25)
print w.find('python3')

#FINDING  ALL THE NUMBER OF POSSITION OF ELEMRNTS IN A STRING 
print 'occurrences of python in the sting :',w.count('python')
n = w.find('python')
print '1st occurrence at :',n
nx = w.find('python',n+1)
print '2nd occurrence at :', nx
nxx = w.find('python',nx+1)
print '3rd occurrence at :',nxx
print 'the position of python in the string is :',n ,
print nx ,
print nxx

print w.index('python')
print w.index('simple')
print w.index('python',7)
print w.index('python',14)

print w.rindex('python')
print w.rindex('simple')

print w.find('s') #'is'
print w.find('s',22) #'simple'

print len(w)
--------------------------------------------------
'''
'''
--------------------------------------------------
f = 'big data is a problem and by using hadoop and spark we can solve this big data problem,hadoop and spark are for processing data.spark is faster then hadoop,hadoop works on mapreduce .sprak had inmemory competition'
print f
print len(f)
g = f.replace('big','huge')
print g
h = f.replace('problem','challenge')
print h
print '******'
print 'hadoop is found',f.count('hadoop'),'times'
f1 = f.replace('hadoop','HADOOP')
print 'f1 :',f1
f2 = f.replace('hadoop','HADOOP',1) # replaces first occurrence 
print 'f2 :', f2
f3 = f.replace('hadoop','h--',2) #replaces first 2 occurrences 
print 'f3 :',f3
 
f4 = f3.replace('h--','')# to delete don't give apace 
print 'f4 :',f4
 
f5 = f4.replace('big data','')
print 'f5 :',f5
print len(f5)
 
print f.replace('spark','')
 
print '--------------------------------'
 
print 'to remove all spaces in the string :[f.replace(' ','')] :'
print '_________________________________'
print f.replace(' ','')
print '---------------------------------'
 
f6 = f.replace('big data','bigdata',1)
print 'f6 :',f6

print f
print '**************split**************'

x = f.split(' ')
print x
print type(x)
print len(x)
x1 = f.replace(' ','',1).split(' ',1) #replacing after 1st occarance 
print x1
print type(x1)

-------------------------------------------------
'''
'''
-------------------------------------------------
m = '101,sdrao,dad,9246578467,+91'
sp = m.split(',')
print sp
print type(sp)

spl = m.split(',',1)
print spl
print type(spl)

print '    '

print 'now converting CSV-spl in to dictionary :'
xs={}
print 'create empty dictionary xs={}'
xs[spl[0]] = spl[1]
print xs
print type(xs)

m1 = m.split(',')
print m1
print type(m1)
k={}
k[m1[0]] = m1[1:]
print k 
print type(k)
----------------------------------------------------
'''
'''
-----------------------------------------------------
m = '101,sdrao,dad,9246578467,+91','201,shobarao,mom,5713523011,+1'
spl = m[1].split(',',1)
print spl
print type(spl)

m1 = m[0].split(',',1)
m2 = m[1].split(',',1)
print m1
print type(m1)
k={}
k[m1[0]] = m1[1:]
k[m2[0]] = m2[1:]
print k 
print type(k)

print k.keys()
print k.values()
print k.items()

print k['201']
print k['101']

print'    '
mx = '300,bharani,sister,9959770068,+91'
m3 = mx.split(',',1)
k[m3[0]] = m3[1:]
print k
print k.keys()

print'    '

r = 'alwal,rishika,myneice,909'
print r
print type(r)
rs = r.rsplit(',',1)
print rs
print type(rs)
------------------------------------------------
'''
'''
------------------------------------------------
print ' ***********      JOIN    ***************         '

a =['mapreduce','jave','spark','scala','bigdata','business']
# a = 'mapreduce , java , spark , scala , mllib , python'

j = ':'.join(a)
print j
print '    '
j ='+'.join(a)
print j
print'    '
j = ' + '.join(a)
print j
print'    '
j = '++'.join(a)
print j 
print'    '
j = '\n'. join(a)
print j
-------------------------------------------------
'''

print '     -----------------validation----------------------'

# e = isupper()
# g = islower()
# c = isalpha()
# d = isdigit()
# f = isalnum()

'''
------------------------------------------------
# sting validation : very important !!
x = 'herndon'
y = 'NEWYARK'
z = 'laxmiNARAYAN rAo'
a = '1234'
b = 'abc123'
d = '$123abc23@'
z= ' '
z1 ='\t'
z2 = '\n'

print x.isupper()
print x.islower()
print x.isalpha()

print '    ', b.isalpha()
print '    ', b.isalnum()
print '    ', x.isalnum()
print '    ', b.isdigit()

print d.isalnum()
print not d.isalnum()

a= 'shibadevender rao '
print dir(a)
print help(x.split)
print help(x.partition)
-----------------------------------------------
'''
# how to change the case of string, irrelavant/irrespective  to the user submission 

'''
-----------------------------------------------
x = raw_input('Enter your name :').upper()
print  x

y = input('Enter your phone number :').isdigit()
print y
------------------------------------------------
'''

# reversing a string :
'''
st = 'bigdata'
x= st[::-1]
print x
'''

a = (10,25,45,78,65)
print a[:-1]
print a[::-1]#to reverse a string 

