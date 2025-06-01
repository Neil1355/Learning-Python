fruits = {"apple", "Mango", "Banana"}
vegetables = {"tomato", "onion", "potato", "Mango"}


cars = {'Toyota', 'Mazda', 'BMW', 'Infiniti', 'Mercedes'}
car = {'Mazda', 'BMW', 'Infiniti', 'Mercedes'}

cars.add('Acura')
print(cars)

"""cars.clear()
print(cars)"""

vehicles = cars.copy()
print(vehicles)

difference = cars.difference(car)
print(difference)
print(cars)
print(car)

cars.difference_update(car)
print(cars)

cars.discard("Toyota")
print(cars)

cars.intersection_update(car)
print(cars)

fruitsAndVegetables = fruits.intersection(vegetables)
print(fruitsAndVegetables)

dissimilar = cars.isdisjoint(fruits)
print(dissimilar)

RandomRemove = car.pop()
print(RandomRemove)

"""EmptySet = cars.remove("Mercedes")
print(EmptySet)"""