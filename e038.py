#https://projecteuler.net/problem=37

biggest = 0

for i in range(10000):
    for j in range(1,10):
        summe = "".join(str(i*k) for k in range(1,j))
        if len(summe) > 10:
            break
        x = int(summe) if summe != '' else 0
        if x > biggest and len(str(summe)) == 9 and len(set(summe)) == 9 and "0" not in summe:
            biggest = int(summe)

print(biggest)
