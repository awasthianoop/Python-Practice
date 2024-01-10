a=int(input("write any integer"))
b=int(input("write any integer"))

if a<b:
    minn=a

else:
    minn=b

for i in range(minn,1,-1):
    if a%i==0 and b%i==0:
        print(i)
        break



