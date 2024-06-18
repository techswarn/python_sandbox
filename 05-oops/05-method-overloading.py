#Method Overloading
#Overloading refers to making a method perform different operations based on the nature of its arguments.

class Employee:
    def __init__(self, ID=None, firstname=None, lastname=None, salary=None, department=None ):
        self=ID
        self=firstname
        self=lastname
        self=salary
        self=department

    def getFullname(self):
        fullName = self.firstname + self.lastname
        return fullName
    
    def getSalary(self):
        return self.salary * 30
    
    def tax(self, title=None):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)
    
    #method overloading demo
    def demo(self, a, b, c, d=5, e=None):   
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)       

# cerating an object of the Employee class
Steve = Employee()

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)