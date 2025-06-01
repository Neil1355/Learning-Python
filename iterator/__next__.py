StudentList = ['neil','nishi','hasti','dev','het','kahan']

myIterator = StudentList.__iter__()  

print(myIterator.__next__())  
print(myIterator.__next__())
print(myIterator.__next__())
print(myIterator.__next__())
print(myIterator.__next__())
print([x for x in   StudentList if len(x)>4])
print([x for x in StudentList if x.__contains__('a')])


print([x for x in 'ABC'])

print([x for x in [1,2,3,4,5] if x>2])

myList = range(1, 5)
print([x for x in myList if x > 3])
