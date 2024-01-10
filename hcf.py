a=int(input("write any number"))
b=int(input("write any number"))
c=min(a,b)
count=0
for i in range(c,0,-1):
    if a%i==0 and b%i==0:
        count+=1
        
          
if count==1:
    print(a,"and",b,"are co-primes")
else:
    print(a,"and",b,"are not co-primes")













    
