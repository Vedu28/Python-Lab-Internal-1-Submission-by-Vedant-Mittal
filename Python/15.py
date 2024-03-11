#15 all pallindrome from 500 to 1000
for n in range(500,1000):
    temp=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(temp==rev):
        print(temp)
