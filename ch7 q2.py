lis=eval(input("write any list"))
sum=0
list2=[]
for i in lis:
    sum+=i
    list2.append(sum)

for j in range(0,len(lis)):
    if lis[j]>=list2[j]:
        print(lis[j])
