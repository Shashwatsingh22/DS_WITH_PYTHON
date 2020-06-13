print("Enter The Text :")
line=input("")
words=line.split()
counts=dict()
print("The Input Words are:",words)
for itr in words:
    counts[itr]=counts.get(itr,0)+1
print("The Result is :\n",counts)    