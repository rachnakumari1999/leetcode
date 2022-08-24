nums=[-2,1,-3,4,-1,2,1,-5,4]
ma=0
s=0
for i in range(0,len(nums)):
    s+=nums[i]
    #print(s)
    if(s>ma):
        ma=s
    if(s<0):
        s=0
print(ma)