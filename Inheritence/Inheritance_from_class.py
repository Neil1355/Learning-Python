class Vehicle:
    def __init__(self, name, max_speed, mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"
 
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity,color):
        super().__init__(name, max_speed, mileage, capacity)
        self.color = color
 
    def seating_capacity(self):
        print(f'the{self.name} could carry {self.capacity} passengers.')
   
    def Showcolor(self):
        print(f'it is {self.color} in color.')
   
class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity,color):
        super().__init__(name, max_speed, mileage, capacity)
        self.color = color
    def seating_capacity(self):
        print(f'the{self.name} could carry {self.capacity} passengers.')
   
    def Showcolor(self):
        print(f'it is {self.color} in color.')
 
sch_bus = Bus('bus',100,20000,50,"blue")
car = Car('car',150,18000,5,"white")
 
for vaahan in (sch_bus,car):
    vaahan.seating_capacity()
    vaahan.Showcolor()
    