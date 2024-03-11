#b decimal to octal
def func(num):
    if num<=0:
        return ''
    else:
        func(num//8)
        print(num%8, end=' ')
a=int(input("enter a decimal number:"))
print(func(a))
