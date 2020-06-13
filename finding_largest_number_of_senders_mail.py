mail=list()
e_dir=dict()
maxword=None
maxcount=None
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line=line.rstrip()
    if not line.startswith("From"):continue
    line=line.split()
    if line[0]=="From":
        mail=line[1:2]        
        for itr in mail:
                e_dir[itr]=e_dir.get(itr,0)+1
for key,value in e_dir.items():
    if maxcount is None or value>maxcount:
       maxcount=value
       maxword=key
print(maxword,maxcount)                      