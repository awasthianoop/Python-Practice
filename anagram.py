def anagram():
    str1=input("write any string")
    str2=input("write any string")
    match=0
    if len(str1)==len(str2):
        for i in str1:
            match=0
            for j in str2:
                if(i==j):
                    match=1
                    break
            if match==0:
                print("strings are not anagrams")
                break;
            else:
                print("anangrams")
    else:
        print("not anagrams")

anagram()
