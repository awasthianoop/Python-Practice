class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def Purchase(self):
        purchase=int(input("write number of quantity of item to be purchased"))
        self.quantity=self.quantity-purchase

    def IncreaseStock(self):
        increasestock=int(input("write quantity of stock to be increased"))
        self.quantity+=increasestock

    def display(self):
        print(self.name)
        print(self.price)
        print(self.quantity)

Iphone=Item("Iphone 14",56000,120)
Iphone.Purchase()
Iphone.display()
Iphone.display()
