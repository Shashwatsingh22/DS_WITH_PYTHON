"""Q1>. Consider a scenario where a son eats five ice creams every day. The price of each ice 
cream is different. His mother pays the bill to the ice cream vendor at the end of every 
week. Write a python program that can generate the bills for the ice creams and send 
to his mother."""
"""
menue={"ice_cream_1":10,"ice_cream_2":20,"ice_cream_3":30,"ice_cream_4":40,"ice_cream_5":50,}
bill=[]

def main():
    print("__________Menue of Ice-cream____________")
    for i in menue.keys():
        print(i,": $",menue[i])
    for i in range(1,5+1):
        choice=input("Enter the icream name that You Wants: ")
        bill.append(menue[choice])
    print("Complete Bill After 1 Month is :",sum(bill)*30)    
main()  """      

"""Q2>. Make a list of last 10 letters of alphabets, then using the slice operation do the 
following operations.
a. Print the first five letters from the list
b. Print any three letters from the middle.
c. Print the letters from any particular index to the end of the list."""

char=['q','r','s','t','u','v','w','x','y','z']
#a>.
print(char[:5])
#b>.
mid=len(char)//2
print(char[mid:mid+3])
#c>.
print(char[mid+3:])
