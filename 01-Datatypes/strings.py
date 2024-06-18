#strings

print("Hello world")
got = "Game of thrones.."
print(got)
multiple_lines='''Hello Swarn
 Good day'''
print(multiple_lines)

#Length of a string
random_string = "I am Batman"  # 11 characters
print(len(random_string))

#accessing charecters in string.
batman="Bruce Wayne"
first=batman[0]
print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman) - 1]
print(last)

#splicing

my_statement="How are you doing?"
print(my_statement[0:3])

my_string = "This is MY string!"
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5

#Partial index
print(my_string[:8])