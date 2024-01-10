def digitcount(num,count=0):
    while num>0:
        rem=num%10
        num=num//10
        count+=1
    return count



def armstrong(summ=0):
    num=int(input("write any number "))
    b=num
    a=digitcount(num)
   
    while num>0:
        rem=num%10
        summ+=rem**a
        num=num//10
    if b==summ:
        print("no is a armstrong number")
    else:
        print("number is not a armstrong number")
    print(summ)

armstrong()
    
