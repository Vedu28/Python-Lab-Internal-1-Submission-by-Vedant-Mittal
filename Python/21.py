# 21 removing duplicates
l=[1,2,3,4,1,6,7,6,8]
print("original list"+str(l))
res=[]
[res.append(x) for x in l if x not in res]
print("after removing duplicates:"+str(res))
