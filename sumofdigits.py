sum=0
num=int(input("write any number"))
while num>0:
    rem=num%10
    sum=sum*10+rem
    num=num//10
print("the reverse of the number is=",sum) 
    
