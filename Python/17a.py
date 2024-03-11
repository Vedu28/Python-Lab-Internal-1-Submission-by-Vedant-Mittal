#17 scripts using functions
#a pallindrome
def pallindrome(n):
    
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
n=int(input("enter a number:"))
print(pallindrome(n))
