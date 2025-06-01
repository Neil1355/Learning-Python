class Employee: 

 def __init__(self, name, employeeId, salary): 
    self.name = name   
    self._empID = employeeId  
    self.__salary = salary   

 def getSalary(self): 
    print(f"The salary of Employee is {self.__salary}") 

employee1 = Employee("John Gates", 110514, "$1500") 

print(f"The Employee's name is {employee1.name}") 
print(f"The Employee's ID is {employee1._empID}") 
employee1.getSalary()