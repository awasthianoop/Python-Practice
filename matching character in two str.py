#to count number of matching characters in two strings.
a=input("write your string")
b=input("write your string")
count=0
for i in a:
    for j in b:
        if i==j:
            count+=1
            
print(count)           
        
