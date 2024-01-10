class RECTANGLE:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def setLength(self):
        self.length=length

    def setBreadth(self,breadth):
        self.breadth=breadth

    def getLength(self):
        return self.length

    def getBreadth(self):
        return self.breadth

    def area(self):
        print(self.getLength()*self.getBreadth())

    def perimeter(self):
        print(2*(self.length+self.breadth))

p1=RECTANGLE(6,2)
p1.setBreadth(10)
p1.area()
p1.perimeter()
