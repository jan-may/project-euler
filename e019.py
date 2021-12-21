#https://projecteuler.net/problem=19

from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

if __name__ == '__main__':
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    print(sum(sd.isoweekday() == 7 and sd.day == 1 for sd in daterange(start_date, end_date)))