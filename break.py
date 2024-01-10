num=int(input("write any value of number"))
f=0
for n in range(2,num,1):
    if num%n==0:
        f+=1
        break
if f==1:
    print(num,"is not prime")
else:
    print(num,"is  prime")
