f=open("abc.txt","r")   
b=f.read()
f.close()

f=open("def.txt","w")
f.write(b)
f.close()


