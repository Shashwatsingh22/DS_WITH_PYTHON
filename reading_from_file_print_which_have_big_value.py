fname=input("Enter The File Name:")
fopen=open(fname)
word=dict()

maxword=None
maxcount=None
for line in fopen:
    #line=line.rstrip()
    words=line.split()
    for itr in words:
        word[itr]=word.get(itr,0)+1

for key,value in word.items():
    if maxcount is None or value>maxcount:
        maxcount=value
        maxword=key    
print("The Max times repeating word in",fname,"is:")
print("Word=",maxword,"\nValue=",maxcount)