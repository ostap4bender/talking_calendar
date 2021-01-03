from datetime import datetime, date, time
# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)


print(datetime.combine(d, t))
# Using datetime.now() or datetime.utcnow()
print(datetime.now())
print(datetime.utcnow())
# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt:
    print(it)
print('_____')
# Date in ISO format
ic = dt.isocalendar()
for it in ic:
    print(it)

# Formatting datetime
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))


today = datetime.combine(date(2021, 1, 21), time(12, 12))
print(today, '!', today.weekday())



