"""Swapping
Description
You are given two integer variables,  x and y. You have to swap the values stored in x and y.

----------------------------------------------------------------------
Input:
Two numbers x and y separated by a comma.

Output:
Print 5 lines. The first two lines will have values of variables shown before swapping, and the last two lines will have values of variables shown after swapping. The third line will be blank.

----------------------------------------------------------------------
Sample input:
20, 50

Sample output:
x before swapping: 20
y before swapping: 50

x after swapping: 50
y after swapping: 20"""

x=int(input("Enter the First Value: "))
y=int(input("Enter the First Value: "))

print("x before swapping:",x,"\ny before swapping:",y)

temp=x
x=y
y=temp

print("x after swapping:",x,"\ny after swapping:",y)