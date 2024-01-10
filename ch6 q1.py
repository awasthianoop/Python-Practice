str1=input("write any sentence")
str2=" "
for i in range(0,len(str1)):
    if str1[i]==str1[i-1]:
        str2=str2[:i+1]+"*"
    else:
        str2+=str1[i]

print(str2)        
