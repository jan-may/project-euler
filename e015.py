#https://projecteuler.net/problem=15

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

import eulerlib

# binomial coefficient () 
def binomial(n):
	return int(eulerlib.numtheory.nCr(n*2, n))


if __name__ == "__main__":
	print(binomial(20))
