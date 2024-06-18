class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)

#Initializer with optional parameters

class Person:
    def __init__(self, ID=None, salary=0, username=None):
        self.ID = ID
        self.salary = salary
        self.username = username

Pikilo = Person(ID=3434, salary=23444, username="pikilllo")
print(Pikilo.username)