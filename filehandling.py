#f=open("abc.txt","w")
#f.write("hi hellow how are you")
#f.close()
f1=open("abc.txt","r")
f1.seek(5)
a=f1.readlines()

print(a)

f1.close()

