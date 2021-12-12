# https://projecteuler.net/problem=3

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# The prime factors of 13195 are 5, 7, 13 and 29.
def largest_primefactor(n):
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            n = n // i
        i += 1
    return n

if __name__ == '__main__':
    print(largest_primefactor(600851475143))
