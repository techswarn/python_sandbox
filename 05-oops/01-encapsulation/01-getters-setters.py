#Encapsulation in OOP refers to binding data and the methods to manipulate that data together in a single unit, that is, class.
#One has to implement public methods to let the outside world communicate with this class. These methods are called getters and setters. We can also implement other custom methods.

class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())
