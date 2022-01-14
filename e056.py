# https://projecteuler.net/problem=56

max = 0
for i in range(100):
    for j in range(100):
        digital_sum = sum(int(digit) for digit in str(i**j))
        if digital_sum > max:
            max = digital_sum

print(max)
