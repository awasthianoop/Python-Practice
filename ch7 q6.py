f=open("poem.py","r")
b=f.read()
alp=0
bs=1
lc=0
uc=0
g=0
g=b.count("beautiful")
vc=0   
for i in b:
    for j in i:
        alp+=1
        if j in "aeiou" and "AEIOU":
            vc+=1    
        if j==" ":
            bs+=1
        if ord(j)<=90:
            uc+=1
        if ord(j)>=97:
            lc+=1

print(alp)
print(bs)
print(uc)
print(lc)
print(g)
print(vc)
f.close()
