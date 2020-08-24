"""Reduce Function
Description
You are given a list of numbers such as 
input_list = [31, 63, 76, 89]. 
Find and print the largest number in input_list using the reduce() function.

Sample Input:
[65,76,87,23,12,90,99]

Sample Output:
99"""
from functools import reduce
input_list=[65,76,87,23,12,90,99]
def greater(x,y):
    if x>y:
        return x
    else:
        return y

print(reduce(lambda x,y:x if x>y else y,input_list))