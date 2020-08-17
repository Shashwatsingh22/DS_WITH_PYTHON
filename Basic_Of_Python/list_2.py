#List_remove_append

"""Description
Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK' in its place.

Sample Input:

['SAS', 'R', 'PYTHON', 'SPSS']

Sample Output:

['SAS', 'R', 'PYTHON', 'SPARK']"""

input_list=['SAS', 'R', 'PYTHON', 'SPSS']
input_list.remove('SPSS')
input_list.append("SPARK")
print(input_list)