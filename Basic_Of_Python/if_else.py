#If-Else
"""Description
Write a code to check if the string in input_str 
starts with a vowel or not. Print capital YES or NO.

For example, if input_str = 'analytics' then, your output should print 'YES'.

Sample Input:

alpha

Sample Output:

YES"""
input_str = 'analytics'
vowels=["a","e","i","o","u"]
if input_str[0] in vowels:
    print("YES")
else:
    print("NO")     