"""1)	Write a program, which takes input of tuples and forms tuple of tuples 
        and then sort the tuple based on the second value in each tuple."""


"""def sorted_tuple(main_tuple):
    main_greater_tuple=()
    max=0
    for i in main_tuple:
        if max<i[1]:
            main_greater_tuple=main_greater_tuple+(i,) 
        else:continue
    return main_greater_tuple"""        

def main():
    tuple_1=()
    main_tuple=()
    big_size=int(input("Enter Number Of smalls tuples: "))
    for j in range(1,big_size):  
      size=int(input("Enter the size of smalls tuples: "))
      for i in range(1,size+1):
        element=int(input("Enter the Element: "))
        tuple_1=tuple_1+(element,)
      main_tuple=main_tuple+(tuple_1,)
    print("Main_tuple: ",main_tuple)
main()        
