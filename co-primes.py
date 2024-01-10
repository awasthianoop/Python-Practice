a=int(input("write any number"))
b=int(input("write any number"))
count=0

if a<b:
    minn=a
elif a>b:
    minn=b

for i in range(1,minn+1):
    if a%i==0 and b%i==0:
        count+=1

if count==1:
    print("numbers are co-prime")
else:
    print("numbers are not co-prime")

print(count)
        
