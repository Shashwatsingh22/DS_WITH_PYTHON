#List to String
"""
Description
Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] 
to a string using ‘&’. The sample output of this string will be:

Pythons syntax is easy to learn & Pythons syntax is very clear
"""
list_1 =['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
list_1=list_1[0] + " & " +list_1[1]
print(str(list_1))