'''
Created on 8 Apr 2018

@author: laxminarayan rao
'''
#Tuples are smiler  to list and  elements are immutable , tuple elements are write protector !! 
t=('unix','linux','perl','unix','risjika','harshika','python','java','aws','devops','odds','matters','blessings','rishika','harshia','gamagamaa','aws','java','high','rash','crash')
#print type(t) ,len(t)
#t[2]='perl1' #AttributeError:'tuple' object does not support item assignment
#del t[3]  #AttributeError:'tuple' object doesn't support item deletion
#t.append('slrao') #AttributeError: 'tuple' object has no attribute 'append'
#print t.count('harshika')

'''for i in t :
    print i'''
'''print t[2],t[-6],t[-6:],t[:6]
print t[::2]
print t[::3]

print t # we can't change the elements in the tuple!!

print t[::-1]
'''
'''for i,j in  enumerate(t): # returns all elements with indexing 
    print i,".",j '''
    
lx = list(t)
#print lx,type(lx)

#lx[3]='sdrao'
lx[4]='rishika'
print lx
print type(lx)
t=tuple(lx)
print t
print type(t)

lx= list(t)
#del lx[7]
del lx[13]
#del lx[14]
#del lx[16]
#del lx[17]
print lx







