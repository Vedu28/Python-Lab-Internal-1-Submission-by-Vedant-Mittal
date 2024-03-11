#8 factorial of a given number
def fact(num):
    product=1
    for i in range(1,num+1):
        product = product*i
    print(product)
num=int(input("enter the number:"))
fact(num)
