# print the contents of the file in upper case.try to remove the whitspace....
fname = input("Enter file name: ")
fh = open(fname)
for itr in fh:
    up=itr.upper().rstrip()
    print(up)
