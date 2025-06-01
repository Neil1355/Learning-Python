#The zip() is a built-in function that takes one or more iterables as input. It returns an object that contains the elements of the input iterables mapped based on the index.
colors = ['red', 'green', 'blue']
codes = [1, 2, 3]

z = zip(colors, codes)
print(list(z))

print('\nnumber-2:\n')

names = ["Ayaan", "Vishva", "Mira"]
scores = [80, 90, 85]

zipped = zip(names, scores)

print(list(zipped))

#unzipping
tup1,tup2,tup3,tup4=zip('wxyz',[0,1,2,3])
print(tup1," ->",tup2," ->",tup3," ->",tup4)