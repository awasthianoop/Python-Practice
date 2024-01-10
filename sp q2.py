def primeornot():
    num=int(input("write a integer number"))
    if num==1 or num==2 or num==3:
        print("1")
    else:
        for i in range(2,num):
            if num%i==0:
                print("0")#means num is not prime
                break

        else:
            print("1")#means num is prime

primeornot()
        
