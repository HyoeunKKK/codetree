n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

sqr = 1600000000

for i in range(n):
    del_point = points[0:i] + points[i+1:n]
    del_x = x[0:i] + x[i+1:n]
    del_y = y[0:i] + y[i+1:n]
    x_diff = max(del_x) - min(del_x)
    y_diff = max(del_y) - min(del_y)
    sqr = min(sqr,x_diff*y_diff)

print(sqr)
