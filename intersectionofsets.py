set1=eval(input("write any set"))
set2=eval(input("write any set"))
set3=set()
for i in set1:
    for j in set2:
        if i==j:
            set3.add(i)
            break
print(set3)
