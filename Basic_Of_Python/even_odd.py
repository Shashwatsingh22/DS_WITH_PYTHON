"""Even Or Odd
Description
Given an integer, print whether it is Even or Odd.

----------------------------------------------------------------------
Input:
An integer

Output:
'Even' or 'Odd'

----------------------------------------------------------------------
Sample input:
3

Sample output:
Odd

----------------------------------------------------------------------
Sample input:
6

Sample output:
Even"""
num=int(input())
if num%2==0:
    print("Even")
else:
    print("odd")