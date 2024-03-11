#14 armstrong number
num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10
if num == sum:
    print("armstrong")
else:
    print("not armstrong")
