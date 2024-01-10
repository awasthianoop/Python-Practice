def sumofd(num,summ=0):
    while num>0:
        rem=num%10
        summ+=rem
        num=num//10
    print(summ)

num=int(input("write any integer"))
sumofd(num)
