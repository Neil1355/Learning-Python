list = []

list.append(10)
list.append(20)
list.append(30)
list.append("Neil")
list.append(5.3)
print(list)

list1 = ['physics', 'chemistry', 'maths', 'english']
print("value available at index 2: ")
print(list1[2])

list1[2] = 'biology'
print("new value available at index 2: ")
print(list1[2])

del list1[2]
print("after deleting value at index 2: ")
print(list1[2])


list2 = ['spam','Spam','SPAM']

print(list2[2])
print(list2[-2])
print(list2[1:])

#comparing 2 lists
if list1 == list2 :
 print("lists are equal")
else:
    print("lists are different")
    
listone = list1.copy()

fruits = ["apple", "mango", "banana"]
list1.extend(fruits)


for i in range (len(list)) :
    print(list[i], end = " ->")
print()
for val in list:
    print(val, end = " :: ")
print()
for i in range(len(list)-1,-1,-1):
    print(list[i], end = " ")
    
    
a =[]
a.insert(2,99)
print("new items are: ",a)

b = [11,22,33]
a.extend(b)
print("new items are: ",a)

del a[0]
print("new items are: ",a)

a.pop()
print("new items are: ",a)

a.remove(22)
print("new items are: ",a)

newlist = a.copy()
print("new list: ",newlist)

"""myList = []"""
myList = a
print("my list: ",myList)


#to add two list values in one
print(list1)
print(list2)
list3 = list1 + list2
print(list3)
list3.sort()
print ("new list: ",list3)


#new list with square of each number from first list
# sort: This causes error because list1 has strings and list2 also has strings.
# To sort successfully, all elements must be of same type.
# So let's make a purely string list
try:
    list3.sort()  # Might cause error if elements are not comparable
    print("new list: ", list3)
except TypeError as e:
    print("Error during sorting list3:", e)
 
# new list with square of each number from a list
flist = [1, 2, 5, 10]
squares = []
for x in flist:
  squares.append(x**2)
print("Squares: ", squares)
 
# check if a value exists in a list
list4 = [10, 20, 2.5, 1, 50]
if 3 in list4:
    print(True)
else:
    print(False)