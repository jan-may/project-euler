#https://projecteuler.net/thread=26;page=8

limit = 1000

longest_cycle = 0
longest_denominator = 1
for n in range(2, limit):
    reminders = {10**d%n for d in range(1, n)}
    if len(reminders) > longest_cycle:
        longest_cycle = len(reminders)
        longest_denominator = n

print(longest_denominator)