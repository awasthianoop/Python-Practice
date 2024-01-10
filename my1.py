num1=int(input("write any value of number"))
num2=int(input("write any value of number"))
for i in range(num1,num2,1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
