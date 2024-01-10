num=int(input("write any number"))
sum=0
for n in range(1,4,+1):
    rem=num%10
    sum=sum*10+rem
    num=num//10
    print(sum)
