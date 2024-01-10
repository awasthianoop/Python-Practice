def studentdata(n):
   
    dic={}
    for i in range(1,n+1):
        rollnum=int(input("write roll number of student"))
        name=input("write name of student")
        dic.update({rollnum:name})
    print(dic)

n=int(input("no of students to be taken"))
studentdata(n)
