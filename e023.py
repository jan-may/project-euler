# https://projecteuler.net/problem=23

border = 28123

def is_abundant(n):
    if sum(i for i in range(1, n//2 + 1 ) if n%i == 0) > n:
        return n

def calculate(my_set=set()):
    lst = [is_abundant(i) for i in range(border) if is_abundant(i)]
    for num in lst:
        for x in lst:
            if num+x < border:
                my_set.add(num+x)

    return (sum(i for i in range(border) if i not in my_set))

if __name__ == '__main__':
    print(calculate())

