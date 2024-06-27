"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]


myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.get_stack())
top =  myStack.pop()
print(top)
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
print(myStack.is_empty())
print(myStack.peek())