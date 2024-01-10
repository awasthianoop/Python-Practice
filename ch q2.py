f=open("anagram.py","r")
a=f.readlines()
count=1
v=0
for i in a:
    for j in i:
        if j==" ":
            count+=1
        if j in "aeiou":
            v+=1
            
print(count)        
print(v)
f.close()
