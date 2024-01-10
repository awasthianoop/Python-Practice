

count=0
num1=int(input("write any number"))
num2=int(input("write any number"))
for num in range(num1,num2):
    def power(num):
        while num>0:
            num=num//10
            count=+1
        return count
    k=power(num)

    def arm(num,sum=0):
        while num>0:
            rem=num%10
            sum=sum+rem**k
            num=num//10
        return sum
    
    c=arm(num)
    if num==c:
        print(num)
    
    
