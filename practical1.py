a=int(input("enter coefficient of x^2"))
b=int(input("enter coefficient of x"))
c=int(input("enter constant"))
root1=(-b+((b**2)-4*a*c)**0.5)/(2*a)
root2=(-b-((b**2)-4*a*c)**0.5)/(2*a)
print("first root of quadratic equation is",root1)
print("second root of quadratic equation is",root2)
