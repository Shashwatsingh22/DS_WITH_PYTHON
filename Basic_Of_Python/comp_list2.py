"""List Comprehensions
Description
Extract the words that start with a vowel from a list
input_list=[wood, old, apple, big, item, euphoria] 
using list comprehensions.

Sample Input:
['wood','old','apple','big','item','euphoria']

Sample Output:
﻿['old', 'apple', 'item', 'euphoria']"""
input_list=["wood", "old", "apple", "big", "item", "euphoria"]
output_list=[i for i in input_list if i[0] in "aeiou"]
print(output_list)