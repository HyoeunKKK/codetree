n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class rainyday:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

days = []

for i in range(n):
    if weather[i] == 'Rain':
        days.append(rainyday(date[i],day[i],weather[i]))

date_list = []
for day in days:
    date_list.append(day.date)

date_list.sort()

target_date = date_list[0]

for day in days:
    if target_date == day.date:
        print(day.date, day.day, day.weather)