a=input("write any character or digit or special character")

d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}


if ord(a)>=47 and ord(a)<=57:
    print("numeric digit",d.get(a))
elif ord(a)>=65 and ord(a)<=90:
    print("upper case character")
elif ord(a)>=97 and ord(a)<=122:
    print("lower case character")
else:
    print("special character")

