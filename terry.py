f1=open("anagram.py","r")
a=f1.readlines()
count=0
for i in a:
    for j in i.split():
        
        print(j)
        if j[0]=="a" or j[0]=="e" or j[0]=="i" or j[0]=="o" or j[0]=="u":
            count+=1
print(count)
f1.close()


        
