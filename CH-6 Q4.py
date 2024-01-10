a=input("write any word")
b=" "
for i in a:
    if i==a[0] and ord(i)<=90:
        b+=i
        
    elif i==a[0]:
        b+=chr(ord(i)-32)

    elif ord(i)>=97:
        b+=i
        
    
    else:
        b+=chr(ord(i)+32)
        
print(b)
