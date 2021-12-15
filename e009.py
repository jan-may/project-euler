'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
if __name__ == '__main__':
    print(pythagorean_triplet(1000))
