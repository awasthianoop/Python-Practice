class Student:
    def __init__(self,rollnum,name,markslist,stream):
        self.rollnum=rollnum
        self.name=name
        self.markslist=markslist
        self.stream=stream
        
    def percentage(self):
        sum=0
        for i in self.markslist:
            sum=sum+i
        per=(sum/5)
        return per
    def gradeGen(self):
        for i in self.markslist:
            if(i>=90):
                print("A")
            elif i>=80 and i<90:
                print("B")
            elif i>=65 and i<80:
                print("C")
            elif i>=40 and i<65:
                print("D")
            elif i<40:
                print("E")
    
    def division(self):
        a=Student.percentage(self)
        if a>=60:
            print("I")
        elif a<60 and a>=50:
            print("II")
        elif a<50 and a>=35:
            print("III")
            
    def __str__(self):
        return "Name="+self.name+" Roll no="+str(self.rollnum)+"  Strem="+self.stream+" Marks="+str(self.markslist)

ram=Student(3940,"ram",[84,80,82,67,73],"Arts")
print(ram)
D=Student.percentage(ram)
print(D)
Student.gradeGen(ram)
Student.division(ram)

    
            
