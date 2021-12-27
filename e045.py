triangle_numbers = [int(n * (n+1) / 2) for n in range(100000)]
triangle_numbers = triangle_numbers[triangle_numbers.index(40755)+1:]
pentragonal_numbers = [int(n * (3*n - 1) / 2) for n in range(100000)]
pentragonal_numbers = pentragonal_numbers[pentragonal_numbers.index(40755)+1:]
hexagonal_numbers = [int(n*(2*n-1)) for n in range(100000)]
hexagonal_numbers = hexagonal_numbers[hexagonal_numbers.index(40755)+1:]

for x in triangle_numbers:
    if x in pentragonal_numbers and x in hexagonal_numbers:
        print(x)
        break