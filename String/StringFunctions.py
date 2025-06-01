'a' in 'battle'
'a' not in 'battle'
name = 'Neil Barot'

print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.casefold())
print(name.center(20))
print(name.count('e'))
print(name.encode())
print(name.endswith('l'))
print(name.expandtabs(2))
print(name.find('Barot'))
print(name.index('B'))
print(name.isalnum())
print(name.isalpha())
print(name.isalpha())
print(name.isascii())
print(name.isidentifier())
print(name.isprintable())
print('_'.join(name))
print(name.replace('Neil','Nishi'))
mytable = str.maketrans('i','e')
print(name.translate(mytable))
print(name.split())

str1 = 'hello'
str2 = 'world!'

print("str1 + str2 = ",str1 + str2)
print('str1 * 3 =', str1 * 3)

String = input("enter string: ")
character = input("enter the character u want to search: ")

count = 0

for letter in 'hello world':
    print(letter)
    if(letter =='l'):
        count +=1
        
print(count, " letters found")

word = 'cold'

list_enumerate = list(enumerate(word))

print('list(enumerate(word))= ',list_enumerate)
print('len(word): ',len(word))

print('''He said, "What's there?"''') 
print('he said, "what\'s there?"')
print("he said, \"what's there?\"")

print("C:\\Python32\\Lib")
print("This is printed\nin two lines") 
print("This is \x48\x45\x58 representation")


str3 = 'hello123xoxo1245'
counter =0
for letter in str3:
    if letter.isnumeric():
        counter+=1
        
print('there are',counter,' numbers in the string')


str4 = 'abc'
str5 = 'abcdefghijklmnopqrstuvwxyz'


"""for char in str4:
    x = str5.find(char)
    char.replace(x+1)
print('new word: ',str4)"""

new_string = ''.join(chr(ord(char) + 1) if char.isalpha() else char for char in str4)
print(new_string)


#to reverse a string

str6 = input("provide a string: ")
str7 = ''.join(reversed(str6))
print(str7)

#count words in a string

str8 = input('enter a statement: ')
z = str8.split()
str9 = ("total words: ",len(z))

#count “is” from the string
str10 = input("write a statement to count number of 'is: ")
counttt =0
for t in str10.split():
    if t == 'is':
        counttt+=1

print('total "is\'s": ',counttt )

    