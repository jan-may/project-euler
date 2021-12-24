#https://projecteuler.net/problem=37

import eulerlib

def is_truncatable_prime(n):
    x = n
    if not eulerlib.is_prime(n): return False
    for i in range(1, len(str(x))):
        if not eulerlib.is_prime(int(str(n)[i:])):
            return False
    return all(eulerlib.is_prime(int(str(n)[:-j])) for j in range(1, len(str(n))))

if __name__ == '__main__':
    print(sum(i for i in range(10, 1000000) if is_truncatable_prime(i)))
    
