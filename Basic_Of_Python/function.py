"""Function
Description
Create a function squared(), which takes x and y as arguments and 
returns the x**y value. For e.g., if x = 2 and y = 3 , then the output is 8.

Sample Input:
['6','7']

Sample Output:
279936"""

def power_of_num(x,y):
    return x**y

num1=int(input("Enter The Number: "))
num2=int(input("Enter the Number: "))

print(power_of_num(num1,num2))