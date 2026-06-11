n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+100)
    y1.append(b+100)
    x2.append(c+100)
    y2.append(d+100)

# Please write your code here.

coor = [list(0 for _ in range(200)) for _ in range(200)]
total = 0
for i in range(n):
    for x in range(x1[i],x2[i]):
        for y in range(y1[i],y2[i]):
            if coor[x][y] == 0:
                coor[x][y] += 1
                total += 1

print(total)