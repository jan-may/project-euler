import eulerlib

def is_circular_prime(n):
    if not eulerlib.is_prime(n):
        return False
    for _ in range(len(str(n))):
        n = (str(n)[1:] + str(n)[0])
        if not eulerlib.is_prime(int(n)):
            return False
    return True

def calculate(num):
    return sum(1 for i in range(num) if is_circular_prime(i))

if __name__ == '__main__':
    print(calculate(1000000))