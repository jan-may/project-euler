#https://projecteuler.net/problem=33

from fractions import Fraction

total = 0

for i in range(1, 100):
    for j in range(1,100):
        if str(i)[-1] == str(j)[0] and int(str(i)[0]) != 0 and int(str(j)[-1]) != 0 and int(str(i)[0]) / int(str(j)[-1]) == i / j:
            if total == 0:
                total += i/j
            else:
                total *= i/j

print(Fraction(total).limit_denominator(1000).denominator)