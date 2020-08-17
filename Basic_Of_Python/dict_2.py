#Dict_Error
"""Description
From a Dictionary 
input_dict={'Name': 'Monty', 'Profession': 'Singer' }, 
get the value of a key ‘Label’ which is not a part of the dictionary, 
in such a way that Python doesn't hit an error. If the key does not exist in the dictionary,
 Python should return 'NA'.

Sample Input:

{'Name': 'Monty', 'Profession': 'Singer' }

Sample Output:

NA"""
input_dict={'Name': 'Monty', 'Profession': 'Singer' }

x='Label' in list(input_dict.keys())

if x==False:
    print("NA")