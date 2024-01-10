def perfectno(summ=0):
    num=int(input("write any number"))
    for i in range(1,num):
        if num%i==0:
            summ+=i

    if num==summ:
        print("perfect number")

    else:
        print("not perfect number")

    print(summ)
            
perfectno()
