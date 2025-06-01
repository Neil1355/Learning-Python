# Program to filter out only the even items from a list 
my_list = [1, 5, 4, 6, 8, 11, 3, 12] 

new_list = list(filter(lambda x: (x%2 == 0) , my_list)) 
print(new_list) 


# Program to double each item in a list using map() 

my_list = [1, 5, 4, 6, 8, 11, 3, 12] 
new_list = list(map(lambda x: x * 2 , my_list)) 
print(new_list) 


#import functools  
from functools import reduce 

num_list = [1,2,3,4,5] 
def prod(x, y): 
       return x * y 
from functools import reduce 
product = reduce(prod, num_list) 

# function that filters vowels 

def fun(variable): 
 letters = ['a', 'e', 'i', 'o', 'u'] 

 if (variable in letters): 
    return True 
 else: 
    return False 
 
# From a list of words, filter only those starting with a vowel using filter and lambda

words = ('car', 'aeroplane', 'bike', 'bicycle', 'e-scooter')
word_list = list(filter(lambda x: x[0].lower() in ('a', 'e', 'i', 'o', 'u'), words))
print(word_list)
