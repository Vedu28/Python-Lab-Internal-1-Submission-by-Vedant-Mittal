#5 leap year or not
q=int(input("enter the year"))
if q%400==0:
    print("leap year")
elif q%4==0 and q%100!=0 :
    print("leap year")
else:
    print("not a leap year")
