'''
Created on 20 Jan 2018

@author: laxminarayan rao
'''
# list compressions 
'''x = []
for i in range(1,101):
    k =(i*i)
    x.append(k)
print x '''


# writing the same above program in 1 line 

'''x = [ i*i for i in range (1,101)]
print x'''

'''x = [ i*i for i in range(1,101) if i%2==0] 
print x '''

'''x =['hadoop','spark','mapreduce','hive','Hbase','sqoop']
y=[[i.upper(),i.lower(),len(i)] for i in x]
print y'''

'''a= [121,24,523,2,458,23,5,9,658,3,7,789652,65,1248,32987,98563,78245,2136595,4656]
count=0
for i in a:
    count=count+1
print "length of list a",count'''

#WAS to insert elements of list in to different lists !!

'''a= [121,24,523,2,458,23,5,9,658,3,7,789652,65,1248,32987,25,3,4,1,10,25,29,89,563,78245,212595,4656]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]

for i in a:
    if   i>=0    and     i<=9    : l1.append(i)
    elif i>=10   and     i<=99   : l2.append(i)
    elif i>=100  and     i<=999  : l3.append(i)
    elif i>=1000 and     i<=9999 : l4.append(i)
    else : l5.append(i)
print l1
print l2
print l3
print l4
print l5'''

#WAS elements which ends with letter s,h,a and saving in different lists  !1

'''d=['unix','linux','perl','python','java','aws','devops','odds','matters','blessings','rishika','harshia','gamagamaa','high','rash','crash']
ls=[]
la=[]
lh=[]
ld=[]
for x in d:
    if    x[-1]  in  "Ss" : ls.append(x)
    elif  x[-1]  in   "Aa": la.append(x)
    elif  x[-1]  in   "Hh": lh.append(x)
    else : ld.append(x) 
print "elements ends with Ss",ls
print "elements ends with Aa",la
print "elements ends with Hh",lh
print ld'''
    
'''w=['unix','linux','perl','unix','risjika','harshika','python','java','aws','devops','odds','matters','blessings','rishika','harshia','gamagamaa','aws','java','high','rash','crash']
ls =[]
la =[]
lh =[]
lw =[]
ld =[]

for i in w:
    if      i[-1]   in "Ss" : ls.append(i)
    elif    i[-1]   in "Aa" : la.append(i)
    elif    i[-1]   in "Hh" : lh.append(i)
    else                    : lw.append(i)
    
for i in w:
    n=w.count(i)
    if n>1 : ld.append(i) # this gives all the duplicate elements in the list !!
print len(w)  # len() gives total number of elements in set  
print "Elements ends with Ss",ls
print "Elements ends with Aa",la   
print "Elements ends with Hh",lh
print "Rest of the elements",lw
print "Duplicate elements in the list w",ld'''

'''w=['unix','linux','perl','unix','risjika','harshika','python','java','aws','devops','odds','matters','blessings','rishika','harshia','gamagamaa','aws','java','high','rash','crash']
print len(w)'''

#Adding elements to the list in run time :
'''n=input("Enter number of students : ")
names=[]
for i in range(1,n+1) :
    print "Enter students name ",i,":"
    x=raw_input()
    names.append(x)
print "REGISTERED STUDENTS LIST,...."
print names '''

#Adding elements at run time in an application 
'''                           n =input("Enter number of students : ")
                            Names=[]
                            for i in range (1,n+1) :
                                print "Enter student name",i,":"
                            # print "class",i,":"
                            #print "section",i,":"
                            x=raw_input()
                            Names.append(x)
                            print "REGESTERD STUDENT DETAILS.........."
                            print Names'''
'''w=['unix','linux','perl','unix','risjika','harshika','python','java','aws','devops','odds','matters','blessings','rishika','harshia','gamagamaa','aws','java','high','rash','crash']
print type(w),len(w)'''
                            

 
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
    
    
    
  
  
  
  
      
