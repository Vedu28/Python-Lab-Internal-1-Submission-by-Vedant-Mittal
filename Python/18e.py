#e GP
def gp(a, r, n):
    sum=0
    for i in range(0,n):
        term=a*pow(r,i)
        print(term,end=" ")
        sum=sum+term
    print("\n""the sum is ",sum)
        
a=int(input("enter the first term ")) 
r=int(input("enter the common ratio"))
n=int(input("enter the nth term"))
gp(a,r,n)
