#https://projecteuler.net/problem=14

'''
Logest Collatz sequenz

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Which starting number, under one million, produces the longest chain?
'''


def collatz(n):
    chain = 1
    while n > 1:
        n = n/2 if n % 2 == 0 else 3*n +1
        chain += 1
    return chain

def compute(num):
    return (max((collatz(i), i) for i in range(num)))

if __name__ == '__main__':
    print(compute(1000000))




