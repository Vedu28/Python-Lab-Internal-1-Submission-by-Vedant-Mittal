#29 table of 10 until user want by list comprehension
n=int(input("enter the number for table"))
res=[10*i for i in range(1,n+1)]
print(res)
# with lambda function
li=[]
n=int(input("enter the number"))
for i in range (0,n+1):
    li.append(i)
print(li)
table=map(lambda x:x*10,li)
for j in table:
    print(j,end=" ")
