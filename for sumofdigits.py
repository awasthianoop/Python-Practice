num=int(input("write any value of number"))
sum=0
for n in range(1,5):
    rem=num%10
    sum=sum+rem
    num=num/10
print(sum)    
