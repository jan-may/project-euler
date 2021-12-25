import eulerlib

primes = eulerlib.primes_wheel_fact(10000000)
print(max(i for i in primes if eulerlib.is_pandigital(i, 1, len(str(i)))))
