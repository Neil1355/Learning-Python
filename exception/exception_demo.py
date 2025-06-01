class MyError(Exception):
    pass
 
def test(x):
    if x < 0:
        raise MyError("Negative value not allowed")
 
try:
    test(-5)
except MyError as e:
    print("Caught custom exception:", e)
    
    
    
class AgeVerificationError(Exception):
    def __init__(self, age, message = 'age is below the legal limit for a motor vehicle license.'):
        self.age = age
        self.message = message
                
def apply_license(age):
    min_age = 18 
    
    if age < min_age:
        raise AgeVerificationError(age)
    else:
        print('Candidate is eligible for a vehicle license.')
        return
    

try:
    age = int(input('entetr your age: '))
    apply_license(age)
except AgeVerificationError as s:
    print(f'candidate not eligible for vehicle license at the age of {s}')
    
    
class InvalidEntryCodeException(Exception):
    pass

def validate_entry_code(entry_code):
    if not entry_code.startswith("UNI"):
        raise InvalidEntryCodeException("Entry code must start with 'UNI'.")
    if len(entry_code) != 10:
        raise InvalidEntryCodeException("Entry code must be exactly 10 characters long.")
    if not entry_code[3:].isdigit():
        raise InvalidEntryCodeException("Entry code must contain digits after 'UNI'.")
    return True

entry_code = "UNI2024001"

try:
    if validate_entry_code(entry_code):
        print(f"{entry_code} is a valid student entry code.")
except InvalidEntryCodeException as e:
    print(f"Invalid entry code: {e}")

