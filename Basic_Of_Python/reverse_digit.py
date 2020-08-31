"""Reverse The Digits
Description
You will be given a number. You have to reverse the digits of the number and print it.

----------------------------------------------------------------------
Input:
A positive integer greater than zero

Output:
The number in reverse order. Check sample outputs for more details.

----------------------------------------------------------------------
Sample input:
345200

Sample output:
2543

----------------------------------------------------------------------
Sample input:
6752343

Sample output:
3432576"""

def reverse(n):
    rem=0   
    while n>0 :
        remain=n%10;
        rem=remain + rem*10
        n=n//10
    return rem    

def main():
    r=int(input())
    print("Reverse of",r,"is :",reverse(r))

main()
