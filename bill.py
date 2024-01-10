product=input("write name of your product")
cost=int(input("write price of product"))
qnt=int(input("write quantity of product"))
total=cost*qnt
discount1=10*total/100
amtopay1=total-discount1
discount2=20*total/100
amtopay2=total-discount2
discount=0
amtopay=total-discount
if total>=1000 and total<3000:
    print("----------------------","name=",product,"cost=",cost,"qnt=",qnt,"total=",total,"discount=",discount1,"amount to pay=",amtopay1,"----------------------")
if total>=3000:
    print("----------------------","name=",product,"cost=",cost,"qnt=",qnt,"total=",total,"discount=",discount2,"amount to pay=",amtopay2,"----------------------")
    
if total<1000:
    print("----------------------","name=",product,"cost=",cost,"qnt=",qnt,"total=",total,"discount=",discount,"amount to pay=",amtopay,"----------------------")
   
