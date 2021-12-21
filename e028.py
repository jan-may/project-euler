#https://projecteuler.net/problem=28

# 4n^2 - 6(n - 1)
def calculate(size):
    if size%2 == 0:
        raise ValueError("Size must be even")
    erg = 1
    erg += sum(4 * i * i - 6 * (i - 1) for i in range(3, size + 1, 2))
    return erg

if __name__ == "__main__":
	print(calculate(1001))