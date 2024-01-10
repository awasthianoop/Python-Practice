def LCM(a,b):
    if a>b:
        maxx=a
    else:
        maxx=b
    for i in range(maxx,1000):
        if i%a==0 and i%b==0:
            break
            
    return i

a=int(input("enter any value"))
b=int(input("enter any value"))
c=LCM(a,b)
print(c)
    
