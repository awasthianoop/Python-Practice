string=input("write a sentence")
dic={}
for i in string:
    a=string.count(i)
    #print(i,"-",a)
    dic.update({i:a})

print(dic)
    
