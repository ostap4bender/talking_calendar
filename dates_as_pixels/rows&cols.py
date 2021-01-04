from datetime import datetime, date, time
YEAR = 2021

first = last = 0
flag_first = flag_last = True

for i in range(1, 8):
    beginning = date(YEAR, 1, i)
    ending = date(YEAR, 12, 32-i)
    if beginning.weekday() == 5:
        if flag_first: first += 1
        flag_first = False
    if ending.weekday() == 6:
        pass

    print(beginning.weekday(), ending.weekday(), sep=' ')
