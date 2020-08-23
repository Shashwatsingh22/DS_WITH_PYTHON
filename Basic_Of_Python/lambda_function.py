#Write the lambda function to check whether the odd and even
num=int(input("Enter the Num to check for odd and even: "))
f=lambda x : "even"  if x%2==0 else "odd"
print(f(num))

"""Lambda
Description
Create a lambda function 'greater', 
which takes two arguments x and y and return x if x>y otherwise y.

If x = 2 and y= 3, then the output should be 3.

Sample Input:
['9','3']

Sample Output:
9"""

greater=lambda y,z: y if z<y else z
print(greater(9,3)) 