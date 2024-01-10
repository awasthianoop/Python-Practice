a=(input("write the age of user"))
try:
    if(a.isdigit()):
        print("number")
        if int(a)<21:
           raise SystemError() 
    else:
        raise OSError()
except SystemError:
    print("age requirement not fulfilled")
except OSError:
    print("value entered is not number")
    
finally:
    print(a)
 
