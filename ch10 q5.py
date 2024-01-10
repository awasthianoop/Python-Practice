class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def Purchase(self,qty):
        self.quantity=self.quantity-qty

    def IncreaseStock(self,qty):
        self.quantity+=qty

    def display(self):
        print(self.name)
        print(self.price)
        print(self.quantity)

Iphone=Item("Iphone 14",56000,120)

Iphone.Purchase(23)
Iphone.IncreaseStock(13)
Iphone.display()
