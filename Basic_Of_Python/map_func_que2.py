"""Map Function
Description
Create a list ‘name’ consisting of the combination of the first name 
and the second name from list 1 and 2 respectively. 

For e.g. if the input list is:
[ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]

the output list should be the list:
['Ankur Narang', 'Avik Sarkar', 'Kiran R', 'Nitin Sareen']

Note: Add a space between first name and last name."""

list_in=[ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]
print(list(map(lambda  x,y:x+" "+ y ,list_in[0],list_in[1])))