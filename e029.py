#https://projecteuler.net/problem=29

def calculate(a,b):
    s = set()
    for i in range(2,a+1):
        for j in range(2,b+1):
            s.add(i**j)
    return len(s)

print(calculate(100,100))