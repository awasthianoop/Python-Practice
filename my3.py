num1=int(input("write any number"))
num2=int(input("write any number"))
for num in range(num1,num2):
    for n in range(2,num):
        if num%n==0:
            break
    else:
        print(num )
            
