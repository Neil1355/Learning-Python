#divide whole list by 2 and return
def div_items(some_list):
    div_bt_two = lambda n:n/2
    return map(div_bt_two,some_list)

print(list(div_items([1,2,3,4,5,6,7,8,9,10])))

#filter out odd values
myList = [23,55,12,25,36,14]
new_list = list(filter(lambda x:(x%2 !=0),myList))
print(new_list)

#filter out names with length more than 3

NameList = ['neil','hasti','dev','nishi', 'kahan', 'het']
newList = list(filter(lambda x: len(x)>3, NameList))
print(newList)

from functools import reduce
num_list = [1,2,3,4,5]
def prod(x,y):
    print('x =',x, 'y =',y)
    return x*y

product = reduce(prod, num_list)
print('the product of all numbers: ',product)