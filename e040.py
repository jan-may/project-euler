c = "".join(str(i) for i in range(1,1000000))

x = 1
erg = 1
for _ in range(7):
    erg *= int(c[x-1])
    x*=10

print(erg)