
# https://projecteuler.net/problem=17

import inflect

def word_count(n):
    p = inflect.engine()
    return (sum(len(p.number_to_words(i).replace(" ", "").replace("-", "")) for i in range(1,n+1)))

if __name__ == '__main__':
    print(word_count(1000))