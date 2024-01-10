class person:
    count=0    #global variable
    def __init__(self,name,dob,salary):
        self.name=name
        self.dob=dob
        self.salary=salary
        person.count+=1

   
    def __str__(self):
        return 'name:'+self.name+'\ndob:'+str(self.dob)+'\nsalary:'+str(self.salary)
    

p1=person('abc','02-02-05','45000')
p2=person('wxy','12-06-02','68000')
print(p1)
print(person.count)
    
