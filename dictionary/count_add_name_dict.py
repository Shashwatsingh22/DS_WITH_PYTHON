
point=dict()
names={'Shashwat','Shivansh','Dheeraj','Shashwat','Shivansh','Tinkoo'}
for itr in names:
    if itr not in point:
        point[itr]=1
    else:
        point[itr]=point[itr]+1
print(point)            