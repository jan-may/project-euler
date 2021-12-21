#https://projecteuler.net/problem=25

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate(n, i=1):
    while True:
        if len(str(fibonacci(i))) >= n:
            return i
        i += 1

print(calculate(1000))