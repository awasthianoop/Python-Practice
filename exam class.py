class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def setlength(self):
        self.length=int(input("write any length"))

    def setbreadth(self):
        self.breadth=int(input("write ay breadth"))

    def getlength(self):
        print(self.length)

    def getbreadth(self):
        print(self.breadth)

    def area(self):
        print(self.length*self.breadth)

    def perimeter(self):
        print(2*(self.length+self.breadth))


r1=Rectangle(4,2)
r1.setlength()
r1.setbreadth()
r1.getlength()
r1.getbreadth()
r1.area()
r1.perimeter()

    
        
