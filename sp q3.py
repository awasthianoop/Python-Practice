class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def display(self):
        print(self.length)
        print(self.breadth)

    def perimeter(self):
        print(2*(self.length+self.breadth))

rec1=rectangle(4,2)
rec1.display()
rec1.perimeter()
