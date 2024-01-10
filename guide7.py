A=eval(input("write any string"))
B=eval(input("write any string"))
c=[]
for b in B:
    for a in A:
        if b==a:
            s=a.find(b)
        else:
            s=-1
        c.append(s)
print(c)        
            
            
            
