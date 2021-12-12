# https://projecteuler.net/problem=1

def compute_multiples(num):
    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    print(compute_multiples(1000))