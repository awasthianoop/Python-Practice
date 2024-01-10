num=int(input("write any number"))
sum=0
for i in range(1,num,1):
    if num%i==0:
        sum=sum+i
        
     
if num==sum:
    print(num,"is a perfect number.")
else:
    print(num,"is not a perfect number.")
