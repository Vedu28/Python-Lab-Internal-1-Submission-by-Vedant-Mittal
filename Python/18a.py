#18 python codes for
#a decimal to binary
def func(num):
    if num >1:
        func(num//2)
    print(num%2,end=' ')  
a=int(input("enter a decimal number:"))
print(func(a))
