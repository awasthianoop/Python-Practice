num=int(input("write any number"))
dic={1:"one",2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
a=[]
while num>0:
    rem=num%10
    num=num//10
    a.append(dic.get(rem))

a.reverse()
r=" "
for j in a:
    print(j,end=" ")
     
