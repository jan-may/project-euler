#https://projecteuler.net/problem=5

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

#brute force method
def smallest_multiple(n):
    x = n
    while True:
        for i in range(1, n+1):
            if x % i != 0:
                x += 1
                break
        else:
            return x

# more elegant method
import math

def smallest_multiple_fast(n):
	erg = 1
	for i in range(1, n+1):
		erg *= i // math.gcd(i, erg)
	return str(erg)


if __name__ == '__main__':
    print(smallest_multiple(10))
    print(smallest_multiple_fast(20))