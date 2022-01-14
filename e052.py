# https://projecteuler.net/problem=52

''' It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. '''

from collections import Counter

for i in range(1, 1000000):
    if Counter(str(i*2)) == Counter(str(i*3)) == Counter(str(i*4)) == Counter(str(i*5)) == Counter(str(i*6)):
        print(i)
        break