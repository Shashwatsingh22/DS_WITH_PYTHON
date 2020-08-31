"""Q2.	 Write a python program to get three integer value from user and pass 
         three values to user defined function (name of function:--lets_check). 
         Find out these values are making equilateral, isosceles or scalene triangle?
         If its equilateral, then find the factorial of that number
        (integer entered by user) otherwise print all the Numbers. (Show both cases)"""

def lets_check(num1,num2,num3):
    if num1==num2 and num2==num3:
        return "iso"
    elif num1==num2 and num1!=num2 and num2    

def main():
    side_1=int(input("Enter the First Value: "))
    side_2=int(input("Enter the Second Value: "))
    side_3=int(input("Enter the Third Value: "))