# https://projecteuler.net/problem=4

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrom(x,y):
    return str(x * y) == str(x * y)[ : : -1]
        
def largest_palindrome(length):
    n = int("9" * length)
    return max(i*k for i in range(n+1) for k in range(n+1) if isPalindrom(i,k))

if __name__ == '__main__':
    print(largest_palindrome(3))
    