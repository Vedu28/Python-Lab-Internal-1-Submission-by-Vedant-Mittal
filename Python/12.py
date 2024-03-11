#12 print fibonacci series upto n terms
n= int(input("enter the number:"))
print(fibonacci(n))
n=10
a=0
b=1
next_num=b
count=1
while count<= n:
    print(next_num,end=" ")
    count+=1
    a,b=b,next_num
    next_num=a+b
print()
