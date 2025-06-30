class student():
    def __init__(self,name,rollno,div):
        self.name = name
        self.roll = rollno
        self.division = div
    
    
    """def getValues(self,nm,rn,div):
        self.name = nm
        self.roll = rn
        self.division = div"""
        
    def PutValues(self):
        print("Name: ", self.name)
        print("Roll No: ", self.roll)
        print("Division: ", self.division)
        
if __name__ == '__main__':
    """s1 = student()
    s1.getValues('Neil', 1, 'A')
    s1.PutValues()"""
    
    name = input("Enter name: ")
    roll = int(input("Enter Roll No: "))
    div = input("Enter Division: ")
    s2 = student(name, roll, div)
    s2.PutValues()