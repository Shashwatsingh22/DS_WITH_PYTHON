"""Question(2)	Write a Python program to compute the similarity between two lists.  
        Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

Expected Output:									(10)
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
"""
def intersection_two_list(list_1,list_2,result):
    for i in list_1:
        if i not in list_2:
            result.append(i)
        else:continue    

def main():
    Color_1=["red", "orange", "green", "blue", "white"]
    Color_2=["black", "yellow", "green", "blue"]

    Color_1_Color_2=[]
    Color_2_Color_1=[]
    intersection_two_list(Color_1,Color_2,Color_1_Color_2)
    intersection_two_list(Color_2,Color_1,Color_2_Color_1)
    print("Color_1-Color_2:",Color_1_Color_2)
    print("Color_2-Color_1:",Color_2_Color_1)

main()