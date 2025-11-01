class school:
    def initialize(self):
        self.type = 'primary'
        self.noofstud = 350
        
    def display(self):
        print('type of school:  ', self.type, ' it has ',self.noofstud, 'students.')
        
class teacher(school):
    def setsubject(self):
        self.sub = 'math'
        
    def setexams(self):
        self.tmarks = 100
        self.duration = 60
        self.date = '2023-10-10'
        
        print(self.tmarks, '----', self.date ,'----', self.duration)
        
class student(school):
    def setfees(self):
        self.fees = 50000
        print('fees: ', self.fees)
        
class external(teacher, student):
    def show(self): 
        super().setfees()
        super().setexams()
        super().setsubject()
        
        print("next exam : ", super().tmarks,"for : ", super().sub) 

if __name__ == "__main__":
    obj = external()
    obj.show()
    