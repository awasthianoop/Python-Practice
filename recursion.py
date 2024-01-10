def fact(num):
    f=1
    if num==1:
        return f
    else:
        f=f*num*fact(num-1)
    return f
num=int(input("write any number"))
print(fact(num))
