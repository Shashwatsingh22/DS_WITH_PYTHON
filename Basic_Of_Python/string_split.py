#String Split
"""
Description
Split the string input_str = 'Kumar_Ravi_003' to the person's second name,
 first name and unique customer code. In this example, second_name= 'Kumar', 
 first_name= 'Ravi', customer_code = '003'.

A sample output of the input 'Kumar_Ravi_003' is:

Ravi
Kumar
003
 
Note that you need to print in the order first name, last name and customer code."""

input_str = 'Kumar_Ravi_003'

first_name=input_str[6:10]
last_name=input_str[0:5]
customer_code=input_str[11:]
print(first_name,last_name,customer_code)