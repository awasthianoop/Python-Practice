num=int(input("write any number your choice"))
summ=0
l=[]
for i in range(1,num):
    if num%i==0:
        summ=summ+i
        l.append(i)

print(l)
print(summ)
if num==summ:
    print(num,"is a perfect number")
else:
    print("number is not a perfect number")
