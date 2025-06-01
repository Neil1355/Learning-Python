First = {'title':'guido'}
Last = {'title' : 'rossum'}

full_name = lambda First, Last: f'Full name: {First["title"]} {Last["title"]}'
print(full_name(First,Last))

add = lambda x,y :x+y
print(add(2,3))