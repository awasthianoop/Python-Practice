def coprime():
    num1=int(input("write any number"))
    num2=int(input("write any number"))
    if num1>num2:
        minn=num2
    else:
        minn=num1
    for i in range(2,minn):
        if num1%i==0 and num2%i==0:
            print("not co-prime")
            break
    else:
        print("co-prime")


coprime()
        
