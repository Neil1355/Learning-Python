class A:
    #constructor
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def show(self):
        print(self.x , "---->", self.y)
        
class B(A):
        #constructor
        def __init__(self):
            super().__init__(10,20)
            self.z = 30
            self.a = 40
            
        def display(self):
            print(self.a , "---->", self.z)
            
if __name__ == "__main__":
    obj = B()
    obj.show()
    obj.display()