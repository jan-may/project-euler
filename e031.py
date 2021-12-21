#https://projecteuler.net/problem=31

def compute_coins():
    coins = [1,2,5,10,20,50,100,200]
    ways = [1]+[0]*200
    for coin in coins:
        for i in range(coin,201):
            ways[i] += ways[i-coin]
    return ways[200]

print(compute_coins())





