# Naming rules
# The following rules must be adhered to when naming classes:
# Must start with a letter or underscore
# Should only be comprised of numbers, letters, or underscores

class Employee:
    ID = 3789
    salary = 2500
    department = "Human Resources"
Swarn = Employee()

# printing properties of Steve - an object of the Employee class
print("ID =", Swarn.ID)
print("Salary", Swarn.salary)
print("Department:", Swarn.department)
print(Swarn)

#Assign values outside of CLASS
class Person:
    ID = None
    username = None
    age = None

Sam = Person()
Sam.ID = 2311
Sam.username = "sam_3e"
Sam.age = 34

print(Sam.username)