#Sets Practice
""""Description
Let’s say you have two lists A and B. 
Identify the elements which are common in the two lists A and B and
 return them in a sorted manner. For example 

Sample Input :

A = [5,1,3,4,4,5,6,7]

B = [3,3,5,5, 1 ,7 ,2]

Sample Output:

[1,3,5]

If you observe the sample output here you can see that 

Though value 5 is repeated twice in both lists, in the final output it is present only once.
The values are returned in a sorted manner with values increasing.
"""
A = [5,1,3,4,4,5,6,7]

B = [3,3,5,5, 1 ,7 ,2]

set_A=set(A)
set_B=set(B)

print(list(set_A.intersection(set_B)))
