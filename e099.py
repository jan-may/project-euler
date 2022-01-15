# https://projecteuler.net/problem=99

import math

values = []

lst = open('problem 99.txt').read().split('\n')

for line in lst:
    x = line.split(',')
    values.append(int(x[1])*math.log(int(x[0],10)))

print(values.index(max(values))+1)