#https://projecteuler.net/problem=20

def factorial(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result

def factorial_sum(n):
    return sum(int(num) for num in str(n))


if __name__ == '__main__':
    print(factorial_sum(factorial(100)))