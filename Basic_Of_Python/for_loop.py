#Iterations
"""Description
You are given a list of string elements and asked to return
a list which contains each element of the string in title case
or in other words first character of the string would be in 
upper case and remaining all characters in lower case

Sample Input:
['VARMA', 'raj', 'Gupta', 'SaNdeeP']

Sample Output:
['Varma', 'Raj', 'Gupta', 'Sandeep']"""

l=['VARMA', 'raj', 'Gupta', 'SaNdeeP']
f=[]
for i in l:
    x=i.lower()
    y=x[0].upper()+x[1:]
    f.append(y)
print(f)    

    