'''
Created on 8 Apr 2018

@author: laxminarayan rao
'''

'''set is in unorder , it wont be the way you created !!
you can add elements to set!! u can add duplicates to set , but it wont return in set !!
it wont support item deletion and  the main concept of set is it holds unique values , i.e it eliminated duplicates !! 
and it allows to do mathamital set operations, i.e union , intersect, minus and sematic differences 
'''
'''S1 ={'sdrao','ssrao','cbrao','csrao','crrao','chrao'}
print S1,type(S1)'''

'''s2={10,121,22,235,568,7,999}
print len(s2)'''
#print s2'''

#print s2[2]#TypeError: 'set' object does not support indexing , set is unorderd collection 
'''s2[2]=701
print s2 #set' object does not support item assignment
del s2[1]#TypeError: 'set' object doesn't support item deletion
'''
'''
a={90,80,70,50,20,10}
b={90,10,20,30,80,60,40}
a|b # | is union 
print a |b
print len(a|b)
a.add(101)
a.add(201)
print a 
print b
print a|b
print len(a|b)
print a&b # intersect 
print len(a&b)
print a - b # returns which are only in a but not in b
print b - a # returns which are only in b but not in a 
print a ^ b # symmetric difference 
print len(a ^ b)
'''
'''
HOW TO REMOVE DUPLICATES IN LIST 
x_list = [10,901,80,12,1556,457,565,21,125,415,1,901,12,565,21,125,415,1556]
print x_list,type(x_list)
print len(x_list)
x_list = set(x_list)
print x_list
print len(x_list)
print type(x_list)
x_list=list(x_list)
print type(x_list)
print x_list
x_list.sort()
print x_list 
'''
''' THIS  IS REMOVING DUPLICATES  IN LIST BY WRITING ONE LINE SCRIPTS !!
x_list = [10,901,80,12,1556,457,565,21,125,415,1,901,12,565,21,125,415,1556]
x_list =list(set(x_list))
print x_list
x_list =sorted(list(set(x_list)))
print x_list'''

a={i for i in range(10)}
print len(a)
print a

