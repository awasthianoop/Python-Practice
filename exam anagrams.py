def anagrams():
    str1=input("write any string")
    str2=input("write any string")
    count=0
    if (sorted(str1)==sorted(str2)):
        print("true-anagrams")
    else:
        print("false-not anagrams")






    #if len(str1)==len(str2):
        #for i in str1:
            #for j in str2:
                #if i==j:
                    #count+=1
                    #break

    #else:
        #print("false-not anagrams")


    #if count==len(str1) and count==len(str2):
        #print("true-anagrams")

    #else:
        #print("false-not anagrams")

anagrams()
                    
