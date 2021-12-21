#https://projecteuler.net/problem=22

import requests

response = requests.get("https://projecteuler.net/project/resources/p022_names.txt")
names = response.text.replace('"', "").split(",")


def total_namescores(lst):
    return sum(
        sum(ord(char) - 64 for char in name) * (i + 1)
        for i, name in enumerate(sorted(names))
    )

if __name__ == '__main__':
    print(total_namescores(names))