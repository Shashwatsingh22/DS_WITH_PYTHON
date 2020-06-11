fname=input("Enter the FileName With extention: ")
count=0
sum=0
try:
  fo=open(fname)
except:
  print("Wrong I/P of the filename.")
  quit()
for itr in fo:
    if not itr.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    t=itr.find("0")
    store=itr[t:]
    f=float(store)
    sum=sum+f
avg=sum/count
print(avg)