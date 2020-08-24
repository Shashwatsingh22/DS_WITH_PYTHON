"""Filter Function
Description
You are given a list of strings such as 

input_list = ['hdjk', 'salsap', 'sherpa'].

Extract a list of names that start with an ‘s’ and end
 with a ‘p’ (both 's' and 'p' are lowercase) in input_list.

Sample Input:
['soap','sharp','shy','silent','ship','summer','sheep']
Sample Output:
['soap', 'sharp', 'ship', 'sheep']"""
list_in=['soap','sharp','shy','silent','ship','summer','sheep']
print(list(filter(lambda x: x[0]=="s" and x[-1]=="p",list_in)))