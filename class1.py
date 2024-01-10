class ABC:
   
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
        
    def add(self):
       print(self.num1+self.num2)

    def sub(self):
        print(self.num1-self.num2)

    def mul(self):
        print(self.num1*self.num2)

    def div(self):
        print(self.num1//self.num2)

    def __del__(self):
        print("deleted")
        

p1=ABC(6,2)
p1.add()
p1.sub()
p1.mul()
p1.div()
del p1
p1.add()
