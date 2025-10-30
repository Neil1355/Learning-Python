def StrReversed(String):
    revstr = String[::-1]
    return revstr

def WordCount(String):
    totalWords = String.split()
    return len(totalWords)

def isCounter(String):
    counter = 0
    net_is = String.split()
    for x in net_is:
        if x == 'is':
            counter+=1
    return counter

def PalindromeWord(String):
    return String == String[::-1]
    
def remove_duplicates(String):
    words = String.split()
    return ' '.join(dict.fromkeys(words))

def is_anagram(String1, String2):
    return sorted(String1) == sorted(String2)

def callit(start,end):
    for i in range(start, end+1):
        print("i -> ",i) 

def StudentList(student_dict):
    student_list = []
    for name, details in student_dict.items():
        student = {
            "name": name,
            "age": details.get("age"),
            "grade": details.get("grade"),
            "id": details.get("id")
        }
        student_list.append(student)
    return student_list

def find_student_by_rollno(rollno, student_list):
    for student in student_list:
        if student["rollno"] == rollno:
            return student
    return None

def edit_student_info(rollno, student_list, updated_info):
    for student in student_list:
        if student["rollno"] == rollno:
            for key in updated_info:
                if key != "rollno" and key in student:
                    student[key] = updated_info[key]
            return True
    return False

def ProductList():
    products = [
        {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10},
        {"id": 2, "name": "Smartphone", "price": 499.99, "stock": 25},
        {"id": 3, "name": "Headphones", "price": 79.99, "stock": 50},
        {"id": 4, "name": "Keyboard", "price": 39.99, "stock": 30}
    ]
    return products

def is_product_in_stock(product_list, product_id):
    for product in product_list:
        if product["id"] == product_id:
            return product["stock"] 
    return False

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
    
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
    
def SumNatNumbers(n):
    if n == 1:
        return 1
    else:
        return n + SumNatNumbers(n - 1)

 

if __name__ == '__main__':
    Str1 = StrReversed('Welcome')
    print(Str1)
    
    str2 = WordCount('hello world')
    print(str2)
    
    str3 = isCounter('how is it going?')
    print(str3)
    
    str4 = PalindromeWord('racecar')
    print(str4)
    
    str5 = remove_duplicates('hello world hello there')
    print(str5)
    
    str6 = is_anagram('listen', 'silent')
    print(str6)
    
    snum = int(input(print('enter the start for the series: ')))
    enum = int(input(print('enter the end for the series: ')))
    callit(snum,enum)
    
    data = {
    "Alice": {"age": 20, "grade": "A", "id": 101},
    "Bob": {"age": 21, "grade": "B", "id": 102}
    }
    students = StudentList(data)
    print(students)
    
    students = [
    {"name": "Alice", "age": 20, "grade": "A", "rollno": 101},
    {"name": "Bob", "age": 21, "grade": "B", "rollno": 102}
]
    result = find_student_by_rollno(101, students)
    print(result)
    
    edit_student_info(101, students, {"name": "Alicia", "grade": "A+"})
    print(students)
    
    product_list = ProductList()
    print(product_list)
    
    products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10},
    {"id": 2, "name": "Smartphone", "price": 499.99, "stock": 0},
    {"id": 3, "name": "Headphones", "price": 79.99, "stock": 50}
]
    print(is_product_in_stock(products, 2))  
    print(is_product_in_stock(products, 1)) 
    
    print("GCD is:", gcd(48, 18))
    
    s = 'abc'
    print(reverse(s))
    
    print(SumNatNumbers(12))