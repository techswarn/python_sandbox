#Let’s write a function which decrements a number recursively until the number becomes 0:

def reduce(n):
    if n == 0:
        return 0
    
    reduce(n-1)
    return n

reduce(10)

#fibonannic
# 0+0 = 0
# 0+1 = 1
# 1+1 = 2
# 1+2 = 3
# 2+3 = 5
# 3+5 = 8

def fib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(8))

#Factorial
# 5! = 5*4*3*2*1 = 25

def fact(n):
    if n == 1:
        return 1
    num = n * fact(n-1)
    return num

print(fact(5))