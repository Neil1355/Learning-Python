sample_dict = { 
    "name": "Kelly", 
    "age": 25, 
    "salary": 8000, 
    "city": "New york" 
} 

# Keys to remove 
keys = ["name", "salary"] 
for k in keys: 
    sample_dict.pop(k) 
print(sample_dict) 

sample_dict2 = {'a': 100, 'b': 200, 'c': 300} 

if 200 in sample_dict2.values():
    print("true")
else:
    print("false")
    
sample_dict3 = { 

  'Physics': 82, 

  'Math': 65, 

  'history': 75

} 
print(min(sample_dict3, key=sample_dict3.get)) 


def dictionary(): 
    key_value = {} 
    key_value[2] = 56 
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24 
    key_value[6] = 18 
    key_value[3] = 323 
    print("Task 1:-\n") 
    print("key_value", key_value) 
    for i in sorted(key_value.keys()): 
        print(i, end=" ") 
        
def main():
    dictionary()

if __name__ =="__main__":
    main()