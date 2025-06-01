# Program to generate a new list by adding 100 to each value using map and lambda
numbers = [10, 20, 30, 40, 50]
add_100 = list(map(lambda x: x + 100, numbers))
print(add_100)

# Program to generate a new list by calculating power of 2 for each number using map and lambda
numbers = [1, 2, 3, 4, 5]
powers_of_2 = list(map(lambda x: x ** 2, numbers))
print(powers_of_2)


dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}] 
filter(lambda x : x['name'] == 'python', dict_a) 

def fahrenheit(T): 
    return ((float(9)/5)*T + 32) 
 
def celsius(T): 
    return (float(5)/9)*(T-32) 

temperatures = (36.5, 37, 37.5, 38, 39) 

F = map(fahrenheit, temperatures) 
C = map(celsius, F) 

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures)) 
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit)) 

print(temperatures_in_Fahrenheit) 
print(temperatures_in_Celsius) 


C = [39.2, 36.5, 37.3, 38, 37.8]  
F = list(map(lambda x: (float(9)/5)*x + 32, C)) 
print(F) 


from functools import reduce 
f = lambda a,b: a if (a > b) else b 
ans = reduce(f, [47,11,42,102,13]) 
print(ans) 

# get length of each string using map and lambda
print(list(map(lambda s: len(s), ["apple", "banana", "kiwi", "grape"])))

# capitalize each word from a list using map and lambda
print(list(map(lambda w: w.capitalize(), ["hello", "world", "python", "rocks"])))

# write a program with map and lambda to process a list to generate a new list by adding 100 to each value
print(list(map(lambda x: x + 100, [10, 20, 30, 40])))
