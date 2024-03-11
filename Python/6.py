#6 prime or composite
num=int(input("enter a number:"))
if num>1:
    for i in range (2, num):
        if(num%i)==0:
            print(num, "composite number")
            break
        else:
            print(num,"prime number")
else:
     print(num,"not prime")
