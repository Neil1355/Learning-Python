import os

file = open('example.txt','w')
file = open('example.txt','r')
file = open('example.txt','a')
file = open('example.txt','rb')


fo = open("foo.txt", "wb") 
print ("Name of the file: ", fo.name) 
print ("Closed or not: ", fo.closed) 
print ("Opening mode: ", fo.mode) 
fo.close() 


# directory/folder path
dir_path = r'C:\\Users\\neilb\\OneDrive\\Desktop\\neil barot\\programs\\Python'
 
# list to store files
res = []
 
# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        res.append(file_path)
print(res)


def list_files(dir_path):
    res = []
    try:
        for file_path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path,file_path)):
                res.append(file_path)
    except FileNotFoundError:
        print(f'the directory{dir_path} does not exist.')
        
    except PermissionError:
        print(f'permission denied to access the directory {dir_path}')
        
    except OSError:
        print(f'An OS error occured: {e}')
    return [res] 

dir_path = r'C:\\Users\\neilb\\OneDrive\\Desktop\\neil barot\\programs\\Java'

files = list_files(dir_path)
print('all files: ',files)


from os import walk
dir_path = 'C:\\Users\\neilb\\OneDrive\\Desktop\\neil barot\\programs\\Java'
res = []
for (dir_path, dir_names, file_name) in walk(dir_path):
     res.extend(file_name) 
print(res)

import os
 
# list to store filename present in current directory
files = []
for file_path in os.listdir('.'):
    if os.path.isfile(os.path.join('.', file_path)):
        files.append(file_path)
for file in files:
    print(file)
    
    try:
        for file_path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path,file_path)):
                res.append(file_path)
    except FileExistsError:
        print('file already exists.')
    
    except PermissionError:
        print(f'permission denied to access the directory {dir_path}')
        
    except OSError:
        print(f'An OS error occured: {e}')