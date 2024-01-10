

class Bank:
    def __init__(self,name,accountnum,Type,amount):
        self.name=name
        self.accountnum=accountnum
        self.Type=Type
        self.amount=amount

    def deposit(self):
        depositt=int(input("write amount you want to deposit"))
        self.amount+=depositt

    def withdrawl(self):
        withdrawll=int(input("write amount o be withdrawn"))
        self.amount-=withdrawll

    def getname(self):
        print(self.name)
        print(self.accountnum)
        print(self.amount)

    def findinterest(self):
        if self.amount>=500000:
            print("interest rate=",8)
            interest=(self.amount*8*1)/100
            print(interest)
        elif self.amount>=300000 and self.amount<500000:
            print("interest rate=",7)
            interest=(self.amount*7*1)/100
            print(interest)
        elif self.amount>=100000 and self.amount<300000:
            print("interest rate=",5)
            
            interest=(self.amount*5*1)/100
            print(interest)
        elif self.amount<100000:
            print("interest rate=",3)
            interest=(self.amount*3*1)/100
            print(interest)
        

    def __str__(self):
        return "name="+self.name+"accountnum="+str(self.accountnum)+"TYPE="+self.Type+"amount="+str(self.amount)

ram=Bank("ram",39402005,"current",400000)
ram.getname()
ram.findinterest()
print(ram)



