#https://projecteuler.net/problem=39

def count_solutions(n):
	count = 0
	for a in range(1, n + 1):
		for b in range(a, (n - a) // 2 + 1):
			c = n - a - b
			if a**2 + b**2 == c**2:
				count += 1
	return count

def calc():
	return max(range(1, 1001), key=count_solutions)
	
print(calc())