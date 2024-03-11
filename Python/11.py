#11 pallindrome or not
n=int(input("enter a number:"))
temp=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("pallindrome")
else:
    print("not pallindrome")
