def A():
    num=int(input("write any number"))
    count=0
    for i in range(2,num):
        if num%i==0:
            count+=1
        
    if count==0:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

def B():
    n=int(input("write the number upto which you want to get list of prime numbers"))
    count=0
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            print(i)
            
            
B()
