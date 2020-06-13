# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
dic=dict()
lst=list()
count=0
name = input("Enter file:")
if len(name) < 1 : name = "test.txt"
handle = open(name)
for line in handle:
    line=line.rstrip()
    if not line.startswith("From"):continue
    line=line.split()
    if line[0]=="From":
        line=line[5].split(":")
        for hr in line[0].split():
            dic[hr]=dic.get(hr,0)+1
for k,v in dic.items():
    lst.append((k,v))
    lst.sort()
for hr,val in lst:
    print(hr,val)    