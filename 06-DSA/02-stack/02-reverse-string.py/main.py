from stack import Stack;

def reverse(string):
    s = Stack()
    length = len(string)
    index = length
    while len(string):
        el = string[index - 1]
        s.push(el)
        index -= 1
        if index == 0:
         break
    return s

result = reverse("hello")
print(result.get_stack())

#Alternative
from stack import Stack
def reverse_string(stack, input_str):
  for i in range(len(input_str)):
    stack.push(input_str[i])
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()

  return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))