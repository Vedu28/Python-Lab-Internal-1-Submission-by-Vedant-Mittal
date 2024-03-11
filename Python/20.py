#20 finding smallest and larest from a list
l=[]
while(True):
    a=int(input("enter number the loop will break on entering a negative number"))
    if a<0:
        break
    else:
        l.append(a);
print(l);
large=small=l[0]
for i in l:
    if i>large:
        large=i
    if i<small:
        small=i
print("largest number:",large)
print("smallest number:",small)
