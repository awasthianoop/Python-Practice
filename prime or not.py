num=int(input("write any number"))
factors=0
for i in range(2,num,1):
    if num%i==0:
        factors+=1
if factors==0:
    print(num,'is a prime number')
else:
    print(num,'is not a prime number')
