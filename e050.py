# https://projecteuler.net/problem=50
import eulerlib

n = 1000000
max = 0
con = 0

primes = eulerlib.prime_numbers.primes(n)
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        x = sum(primes[i:j+1])
        if x >= n:
            break
        if eulerlib.is_prime(x) and len(primes[i:j+1]) > con and x > max:
            con = len(primes[i:j+1])
            max = x

print(max)