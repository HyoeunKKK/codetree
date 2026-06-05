m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mon = m1
date = d1
days = 1

while True:
    if mon == m2 and date == d2:
        break
    days += 1
    date += 1
    if date > months[mon]:
        mon += 1
        date = 1

print(days)