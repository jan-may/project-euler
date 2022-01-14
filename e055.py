# https://projecteuler.net/problem=55

def is_lynchrel(n):
    num = n
    for _ in range(n, n+50):
        num = num + int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            return False
    return True

print(sum(is_lynchrel(i) for i in range(10000)))