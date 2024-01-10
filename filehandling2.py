

f=open("hcf.py","r")
#print(f.readlines())
count=0
for i in f.readlines():
    for j in i:
        if(j=='a'):
            count=count+1   
print(count)
    
f.close()


