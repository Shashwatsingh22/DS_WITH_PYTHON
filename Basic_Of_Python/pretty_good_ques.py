"""Beautiful Pretty Sexy
Description
A number k is beautiful if it is of the form 3n+1, is pretty 
if it is of the form 3n+2 and is sexy if it is of form 3n.
Given a number k, print if it is beautiful, pretty or sexy.

Sample input:
21

Sample output:
sexy

Sample input:
22

Sample output:
beautiful

Sample input:
23

Sample output:
pretty"""
k = int(input())

if k%3==0:
    print("sexy")
elif (k-1)%3==0:
    print("beautiful")
elif (k-2)%3==0:
    print("pretty")        