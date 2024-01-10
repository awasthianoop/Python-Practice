x=int(input("write any integer"))
n=int(input("write any integer"))
summ=1

for i in range(1,n):
    f=1
    r=1
    if (i%2)!=0:
        for j in range(1,i*2+1):
            r=r*x
            f=f*j
        summ=summ-(r/f)

    else:
        for j in range(1,i*2+1):
            r=r*x
            f=f*j
        summ=summ+(r/f)

print(summ)
