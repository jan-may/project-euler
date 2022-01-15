# https://projecteuler.net/problem=63

erg = 0
for i in range(1,50):
    for j in range(1,50):
        if len(str(i**j)) == j:
            erg += 1

print(erg)
