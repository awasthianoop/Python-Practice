f=open("anagram.py","r")
f1=open("abc.py","w")
a=f.readlines()
for i in range(0,len(a),2):
    f1.write(a[i])
    print(a[i])
    

f.close()
f1.close()
