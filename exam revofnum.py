def reverseofnum(num,summ=0):
    while num>0:
        rem=num%10
        summ=summ*10+rem
        num=num//10
    print(summ)

num=int(input("write any integer"))
reverseofnum(num)
