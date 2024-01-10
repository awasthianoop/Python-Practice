def star():
    str1=input("write any string")
    temp=""
    i=0
    l=len(str1)
    while(i<l):
        temp=temp+str1[i]
        for j in range(i+1,len(str1)):
            if(str1[i]==str1[j]):
                temp=temp+"*"
                i=i+1
        i=i+1        
    print(temp)

star()
