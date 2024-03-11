#22 list concatination
def li(lst,n):
    l1=[item+str(i) for i in range(1,n+1) for item in lst]
    return l1
l=['p','q']
n=5
res=li(l,n)
print(res)
