sample=input("write any list")
count=0
for i in sample:
    if i in 'aeiouAEIOU':
        count+=1
print(count)        
