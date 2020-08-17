#Tuple
"""
Description

Add the element ‘Python’ to a tuple input_tuple = ('Monty Python', 'British', 1969).
 Since tuples are immutable, one way to do this is to convert the tuple to a list, 
 add the element, and convert it back to a tuple.

Sample Input:
('Monty Python', 'British', 1969)

Sample Output:

﻿('Monty Python', 'British', 1969, 'Python')
"""
#<-----------------Solution----------------->
input_tuple = ('Monty Python', 'British', 1969)

#Changing To List

input_List= list(input_tuple)
input_List.append("Python")

input_tuple= tuple(input_List)
print(input_tuple)
