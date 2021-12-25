import requests

words = requests.get("https://projecteuler.net/project/resources/p042_words.txt").text.replace('"', "").split(",")

# ½n(n+1)
triangle_numbers = [int(0.5 * i * (i+1)) for i in range(1,30)]

total = 0
for word in words:
    word_sum = sum(ord(char) -64 for char in word)
    if word_sum in triangle_numbers:
        total += 1

print(total)