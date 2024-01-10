from abc import ABC
class car(ABC):
    def mileage(self):
        pass

class mahindra(car):
    def mileage(self):
        print("xuv")

class maruti(car):
    def mileage(self):
        print("swift")

class tata(car):
    def mileage(self):
        print("tigor")

m=mahindra()
m.mileage()
l=maruti()
l.mileage()
