# https://projecteuler.net/problem=48

def self_powers(n):
   erg = sum(i**i for i in range(1,n+1))
   if len(str(erg)) >= 10:
       return str(erg)[-10:]
   return erg

print(self_powers(1000))