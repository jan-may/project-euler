z = 3
n = 2
pz = 0
pn = 0
summe = 0

for _ in range(1000):
    pz = z
    pn = n
    n = pz + pn
    z = pz + pn + pn
    if len(str(z)) > len(str(n)):
        summe += 1

print(summe)