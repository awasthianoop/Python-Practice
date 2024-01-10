num=int(input("write any number"))
sum=0
t=num
for n in range(1,4,+1):
    rem=num%10
    sum=sum+rem**3
    num=num//10
    if t==sum:
        print("number is armstrong")
