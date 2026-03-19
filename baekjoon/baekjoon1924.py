import datetime

x, y = map(int, input().split())

date = datetime.date(2007, x, y)

days = ["MON", "TUE", "WEN", "THU", "FRI", "SAT", "SUN"]

print(days[date.weekday()])