a=int(input("write any integer"))
b=int(input("write any integer"))

if a>b:
    maxx=a

else:
    maxx=b

while(1):
    if maxx%a==0 and maxx%b==0:
        break;
    else:
        maxx+=1;
print(maxx)
