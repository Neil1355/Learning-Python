class grandparent():
    def heritage(self):
        print('this family values wisdom.')
    
class parent(grandparent):
    def values(self):
        print('this family values hard work.')
        
class child(parent):
    def dreams(self):
        print('I want to be a software engineer.')
        
c = child()
c.heritage()
c.values()
c.dreams()

print('\nNumber-2 :\n' )
#using __init__() and super()
class Grandparent:
    def __init__(self, family_name):
        print(f"Family name is {family_name}")

class Parent(Grandparent):
    def __init__(self, family_name, parent_job):
        super().__init__(family_name)
        print(f"Parent works as {parent_job}")

class Child(Parent):
    def __init__(self, family_name, parent_job, child_dream):
        super().__init__(family_name, parent_job)
        print(f"Child wants to become a {child_dream}")

c = Child('Khan', 'Engineer', 'Software Engineer')


print('\nnumber - 3:\n')

class company():
    def __init__(self, company_name):
        print(f'Company:{company_name}')
        
class department(company):
    def __init__(self, company_name, department_name):
        super().__init__(company_name)
        print(f'Department: {department_name}')
        
class employee(department):
    def __init__(self, company_name,department_name,employee_name):
        super().__init__(company_name,department_name)
        print(f'Employee: {employee_name}')
        
c = employee('OPENAI','Research','Ayaan')