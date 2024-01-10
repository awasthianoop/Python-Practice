f1=open("weight.py","r")
f2=open("price.py","r")
a=f1.read()
b=f2.read()
f1.close()
f2.close()


f3=open("weight and prices","w")
c=f3.write("a")
print(c)
f3.close()
        
