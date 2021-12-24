def check_palindorm(n):
    if str(n) == str(n)[::-1] and str(format(n, "b")) == str(format(n, "b"))[::-1]:
        return n
    return 0

if __name__ == '__main__':
    print(sum(check_palindorm(i) for i in range(1000000)))




