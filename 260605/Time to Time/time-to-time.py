a, b, c, d = map(int, input().split())

# Please write your code here.

time = 0
hour = a
mins = b
while True:
    if hour == c and mins == d:
        break
    time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(time)