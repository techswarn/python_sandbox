#range(start, end, step)
for i in range(1, 11):  # A sequence from 1 to 10
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")
#Looping Through a List/String
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)

for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
    float_list[i] = float_list[i] * 2

print(float_list)

#Break keywork
#Sum of two nunbers

value = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False

for n1 in num_list:
    for n2 in num_list:
        if n1 != n2:
            if (n1 + n2 == value):
                found = True
                break
    if (found == True):
        print(n1, n2)
        break

#Continue keywork
num_list = list(range(0, 10))

for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)

#The pass Keyword
num_list = list(range(20))

for num in num_list:
    pass # You can write code here later on

print(len(num_list)) 