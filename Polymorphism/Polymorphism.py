class Monkey: 
    def color(self): 
        print("The monkey is yellow coloured!") 

    def eats(self): 
        print("The monkey eats bananas!") 

class Rabbit: 
    def color(self): 
        print("The rabbit is white coloured!") 

    def eats(self): 
        print("The rabbit eats carrots!") 

mon = Monkey() 
rab = Rabbit() 

for animal in (mon, rab): 
    animal.color() 
    animal.eats() 