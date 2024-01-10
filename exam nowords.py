def noofwords():
    str1=input("write any sentence")
    count=1
    for i in str1:
        if i==" ":
            count+=1
    print("no of words are-",count)

noofwords()
