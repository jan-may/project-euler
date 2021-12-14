# https://projecteuler.net/problem=6

'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''	

def difference(n):
    sum_of_square = 0
    square_sum = 0
    for i in range(1, n+1):
        sum_of_square += i**2
        square_sum += i
    return square_sum**2 - sum_of_square

if __name__ == '__main__':
    print(difference(100))

