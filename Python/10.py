#10 to find reverse of a given number
n=1234
print(str(n)[::-1])
num=int(input("enter a number"))
rnum=0
while num!=0:
    d=num%10
    rnum=rnum*10+d
    num//=10
print("reverse:",str(rnum)) 
