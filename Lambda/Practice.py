def squared(n):
     return n**2

numbers = [1,2,3,4,5]
squared_numbers = print(list(map(squared,numbers)))
print(squared_numbers)

list1 = [1,2,3,4,5]
squaredd = list(map(lambda number : number*2,list1))
print(squaredd)


def uppercase(s):
    return s.upper()

words = ['neil','nishi','hasti','kahan']
UCwords = print(list(map(uppercase,words)))
print(UCwords)

New_Words = ['dev','het','tanay','krish','rahul']
Upperrcase_Words = list(map(lambda UC :UC.upper(),New_Words))
print(Upperrcase_Words)

def Add_prefix(x):
    return (f'Mr.{x}')

name = ['john','jeff','bob','carlos']
prefix_name = print(list(map(Add_prefix,name)))
print(prefix_name)


def Absolute_Values(ab):
    if ab>0:
        return ab
    elif ab<0:
        c = ab*-2+ab
        return c
    
value = [3,-7,2.1,-3,-17]
Abval = print(list(map(Absolute_Values,value)))
print(Abval)


init_words = ['Basketball','cat','walgreens','rutgers','neil']
len_of_words = list(map(lambda Word_length : Word_length.__len__(),init_words))
print(len_of_words)

