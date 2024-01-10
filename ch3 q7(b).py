x=int(input("write any integer for value of x"))
n=int(input("write how much terms to take as n"))

summ=1
for i in range(1,n+1):
    r=1
    f=1
    for j in range(1,i+1):
        r=r*x
        f=f*j
    summ=summ+(r/f)
print(summ)
    
