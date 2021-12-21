# https://projecteuler.net/problem=24

import itertools

def nth_permutation(chars, n):
    p = sorted(itertools.permutations(l, len(l)))
    return ("".join(str(char) for char in list(p[n])))

if __name__ == '__main__':
    l = [0,1,2,3,4,5,6,7,8,9]
    print(nth_permutation(l, 999999))


