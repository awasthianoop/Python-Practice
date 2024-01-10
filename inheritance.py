class animal:
    def display(self):
        print("show method animal")

class dog(animal):
    def show(self):
        print("display in dog")
        
class cat(animal):
    def out(self):
        print("display in cat")

dd=dog()
aa=cat()
dd.display()
aa.display()
dd.show()
aa.out()
