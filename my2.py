def perfectnumber(num,sum=0):
    for n in range(1,num,1):
        if num%n==0:
            sum=sum+n
    
    if num==sum:
        print(num,"is a perfect number")
    else:
        print(num,"is not a perfect number")
        
num=int(input("write any value of number"))
perfectnumber(num)
