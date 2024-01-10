x=int(input("write any value of x"))
n=int(input("write any  value of n"))
sum=1
fac=1
for j in range(n,1,-1):
    fac=fac*j
    
for i in range(1,n+1):
    fac=i
    sum+=(x**i)/fac

print(sum)
