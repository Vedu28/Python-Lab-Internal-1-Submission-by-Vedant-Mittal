#b
def pattern(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\r") 
print(pattern(5))
