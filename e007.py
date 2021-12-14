# https://projecteuler.net/problem=7

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

import eulerlib

def findNthPrime(n):
    count = 0
    y = 1
    while count < n:
        if eulerlib.is_prime(y):
            count += 1
        y+=1
    return y-1

if __name__ == '__main__':
    print(findNthPrime(10001))