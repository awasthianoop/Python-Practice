a=eval(input("write a list"))
b=[]
for i in a:
    if str(i).isnumeric():
        if i%2==0:
            b.append(i**3)
    else:
        print("")
        
print(b)
