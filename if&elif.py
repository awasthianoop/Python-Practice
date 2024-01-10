cost_price=int(input("enter cost price of product"))
sell_price=int(input("enter selling price of product"))
if sell_price>cost_price:
    print("profit")
elif sell_price<cost_price:
    print("loss")
elif sell_price==cost_price:
    print("neither profit nor loss")
    
