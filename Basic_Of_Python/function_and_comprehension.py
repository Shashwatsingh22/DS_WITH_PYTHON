"""Function Parameters
Functions can be used inside a list comprehension too. 
An example to create a list, the elements of which would be 
the result of applying x2−2x−2 
on each element in the list = [2,7,8,10,3]"""

list_1 = [2,7,8,10,3]

def quad_(x):
    return x**2-2*x-2

list_2=[quad_(i) for i in list_1]
print(list_2)  