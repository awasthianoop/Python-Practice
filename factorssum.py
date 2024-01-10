num=int(input("write any number"))
sum=0
for n in range(num,0,-1):
    if num%n==0:
        sum=sum+n
        print(n,)
print(sum)        
        
