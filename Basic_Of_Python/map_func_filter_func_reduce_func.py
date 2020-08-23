#<------Map function----------->
#Write an Example of the map function
list_1=[2,4,5]
list_2=list(map(lambda x:x**2+2*x-2,list_1))
def quad(x):
    return x**2
list_quad=list(map(quad,list_1))
print(list_2)
print(list_quad)

#<----------Filter Function------>
#Write an Example of the filter function
string=["Shashwat" ,"Singh"]
st=list(filter(lambda x:"a" in x,string))
print(st)
#Write an program for filter the list which are divisible by three
list_=[2,36,58,20,42]
def check_by_3(x):
    if x%3==0:
        return True
    else:
        return False    
mlist=list(filter(check_by_3,list_))
print(mlist)

#Filter the student name by there age 18
dict_student={1:["Shashwat",19],2:["Sam",18],3:["rajiv",16],4:["ram",21]}
above_list=list(filter(lambda x:x[1]>18 ,dict_student.values()))
print(above_list)

#<---------Reduce Function------>
#Write an Example of the reduce function
from functools import reduce as r
s=r(lambda x,y:x+y,string)
print(s)