"""Q2. Write a program to record the details of employees in an organization (e.g., Name, ID, Qualification, Address, etc.) in a dictionary as follows:
	Employees = {(Name, ID): (Age, Qualification, Address, etc.), ………………….},
    Divide the employees in the above dictionary into different groups based on their qualification
    and represent each group using separate dictionary
"""
"""
Emp={}
keys_tuple_name_id=[]
values_tuple_info=[]

size=int(input("Enter The Number of the Emp: "))
for i in range(1,size+1):
    print("Enter the name of the emp",i,": ",end=" ")
    name=input()
    print("Enter the emp_id of emp",i,": ",end=" ")
    emp_id=input()
    print("Enter the Age of emp",i,": ",end=" ")
    age=input()
    print("Enter the Qualification of emp",i,"(Inter/High): ",end=" ")
    quali=input()
    print("Enter the Address of the emp",i,": ",end=" ")
    address=input()
    keys_tuple_name_id.append((name,emp_id,))
    values_tuple_info.append((age,quali,address),)

for i,j in zip(keys_tuple_name_id,values_tuple_info):
    Emp[i]=j


inter_qual_emp={}
high_qual_emp={}

for i,j in zip(keys_tuple_name_id,values_tuple_info):
    if j[1]=="Inter":
        inter_qual_emp[i]=j
    else:
        high_qual_emp[i]=j   


print("High_School_Qualification Emp:",high_qual_emp)
print("Intermediate_School_Qualification Emp:",inter_qual_emp)
"""
"""Q1>. Write a program to convert a decimal integer
       into its base 6 equivalent representation.


dec_val=int(input("Enter Integer Number :"))
base_six=[]

while dec_val>0:
    rem=dec_val%6  
    dec_val=dec_val//6
    base_six.append(rem)

for i in base_six:
    print(i,end="")"""

"""Q3>Explain string slicing with the help of a suitable program.
String slicing operator returns a slice of the string using the syntax s[start : end],where s is the string. It is a substring from index start to end-1.

string=input("Enter a string :")
len_1=len(string)
print("Length of string:",len_1)
print( "Doing string slicing" )
print("Lets Slice String Upto Middle: ",string[0:(len_1-1)//2])
print("String Slice from back  ",string[-1:])"""


"""Write a program to generate and print all possible combination of the characters present in a given string.
Take length of string=4.JOHN will have combinations JONH,JNOH....."""
import itertools
print("LENGTH OF STRING MUST BE 4")
s=input("ENTER YOUR STRING")
t=list(itertools.permutations(s,len(s)))
for i in range(0,len(t)):
    for j in t[i]:
        print(j,end="")
    print(end=",")