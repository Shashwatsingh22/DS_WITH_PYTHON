
point=dict()
names={'S','Sh','Dh','Sh','S','T'}
for itr in names:
    point[itr]=point.get(itr,0)+1
print(point)            