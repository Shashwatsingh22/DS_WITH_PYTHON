#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
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
