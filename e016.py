# https://projecteuler.net/problem=16

'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
'''

def power_digits(n, p):
    return sum(int(i) for i in str(n**p))
    
if __name__ == '__main__':
    print(power_digits(2, 1000))