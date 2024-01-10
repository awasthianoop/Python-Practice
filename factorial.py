def factorial(a):
    fac=1
    for i in range(a,1,-1):
        fac=fac*i
    return fac
a=int(input("enter any number"))
b=factorial(a)
print(b)
    
