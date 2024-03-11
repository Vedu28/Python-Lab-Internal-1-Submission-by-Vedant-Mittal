#9 sum of digits of a given number
def getsum(n):
    sum=0
    while(n!=0):
        sum=sum+(n%10)
        n=n//10
    return sum
n=int(input("enter a number"))
print(getsum(n))
