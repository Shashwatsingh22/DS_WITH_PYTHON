"""Map Function
Description
Using the function Map, count the number of words that start with ‘S’ in input_list.

Sample Input:
['Santa Cruz','Santa fe','Mumbai','Delhi']

Sample Output:
2"""
input_list=["Santa Cruz","Santa fe","Mumbai","Delhi"]

print(len(list(filter(lambda x:x.startswith("S"),input_list))))

print(sum(list(map(lambda x:x[0]=="S",input_list))))