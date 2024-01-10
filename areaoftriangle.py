def AofTriangle(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5

    if a+b>c and b+c>a and a+c>b:
        print("yes,sum of length of two sides is greater than the third side")
    else:
        print("no,sum of length of two sides is not greater than the third side")

    print("area=",area)

a=int(input("write value of first side of triangle"))
b=int(input("write value of second side of triangle"))
c=int(input("write value of third side of triangle"))
AofTriangle(a,b,c)
