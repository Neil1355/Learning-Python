class Library: 

    def __init__(self, id, name): 
        self.__bookId = id 
        self.bookName = name 

    def setBookName(self, newBookName): 
        self.bookName = newBookName 

    def getBookName(self):
        print(f"The name of book is {self.bookName}") 

book = Library(101,"The Witchers") 
book.getBookName() 
book.setBookName("The Witchers Returns") 
book.getBookName() 

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
print(f"The Employee's salary is {employee1.salary}") 



# super class

class Student:
 
    # protected data members

    _name = None

    _roll = None

    _branch = None
 
    # constructor

    def __init__(self, name, roll, branch):

        self._name = name

        self._roll = roll

        self._branch = branch
 
    # protected member function

    def _displayRollAndBranch(self):
 
        # accessing protected data members

        print("Roll:", self._roll)

        print("Branch:", self._branch)
 
# derived class

class College(Student):
 
    # constructor

    def __init__(self, name, roll, branch):

        Student.__init__(self, name, roll, branch)
        
    # public member function
    def displayDetails(self):
 
              # accessing protected data members of super class

        print("Name:", self._name)
 
        # accessing protected member functions of super class

        self._displayRollAndBranch()
 
 
stu = Student("Alpha", 1234567, "Computer Science")

print(dir(stu))
 
# protected members and methods can be still accessed

print(stu._name)

stu._displayRollAndBranch()
 
# Throws error

# print(stu.name)

# stu.displayRollAndBranch()
 
# creating objects of the derived class

obj = College("R2J", 1706256, "Information Technology")

print("")

print(dir(obj))
 
# calling public member functions of the class

obj.displayDetails()
 