# https://projecteuler.net/problem=92

def has_eighty_nine(num):
    x = num
    if x == 89:
        return True
    while x != 89 or x != 1:
        summe = sum(int(char)**2 for char in str(x))
        if summe == 89:
            return True
        if summe == 1:
            return False
        x = summe

print(sum((has_eighty_nine(y)) for y in range(1,10000000)))