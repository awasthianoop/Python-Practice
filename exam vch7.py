num=int(input("write any number"))
dic={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
a=[]
while num>0:
    rem=num%10
    num=num//10
    a.append(dic.get(rem))
    
a.reverse()
for i in a:
    print(i,end=" ")
