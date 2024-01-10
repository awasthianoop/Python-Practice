def anagram(a,b):
    count=0
    if len(a)==len(b):
        for i in a:
            for j in b:
                if i==j:
                    count+=1
                    break
        if count==len(a) and count==len(b):
            print("anagram")
        else:
            print('not anagram')
    else:
        print('not anagram')

a=input("write any word")
b=input("write any word")
anagram(a,b)

