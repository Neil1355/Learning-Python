n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print('cant be divided by zero')

def file_op():
   try:
       f = open("nonexistent.txt")
       data = f.read()
   except FileNotFoundError:
       print("File not found.")
   finally:
       print('good to go')

file_op()

class NegativeNumberError(Exception):
   pass

def square_root(x):
   try:
       if x < 0:
           raise NegativeNumberError("Negative input error")
       else:
           print(f"Square root is {x ** 0.5}")
   except NegativeNumberError as e:
       print(e)

square_root(-9)

def reraise():
    try:
        1 / 0
    except ZeroDivisionError as e:
        print('caught error:', e)
        raise 

reraise()

def Nested_exception():
   try:
       int("not a number")
   except ValueError as e:
       raise RuntimeError("Conversion failed") from e

Nested_exception()