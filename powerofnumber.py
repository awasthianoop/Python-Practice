def pow(a,b):
    mul=1
    for i in range(1,b+1):
        mul=mul*a
    return mul
   
a=int(input("enter any number"))
b=int(input("enter any power"))
d=pow(a,b)
print(d)
