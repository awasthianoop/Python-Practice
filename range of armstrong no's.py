n1=int(input("write any integer"))
n2=int(input("write any integer"))


for i in range(n1,n2):
    num=i
    summ=0
    while num>0:
        rem=num%10
        summ+=rem**3
        num=num//10
    if i==summ:
        print(i)
   

    
