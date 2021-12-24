#https://projecteuler.net/problem=34

sum = 0
erg = 0
for i in range(10,100000):
    for char in str(i):
        temp = 1
        for x in range(1,int(char)+1):
            temp *= x
        sum += temp
        if sum == i:
            erg += i
    sum = 0

print(erg)
            



