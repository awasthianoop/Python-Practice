import sys
a=int(input("write any number"))
b=int(input("write any number"))
print("hello")
try:
    c=a/b
    print(c)
except:
    print(sys.exc_info())
    print("zero division error")
finally:
    print("always executed")
print("red,green")
