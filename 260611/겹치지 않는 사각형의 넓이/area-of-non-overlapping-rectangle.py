x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

coor = [list(0 for _ in range(2000)) for _ in range(2000)]
total = 0
for i in range(2):
    for x in range(x1[i]+1000,x2[i]+1000):
        for y in range(y1[i]+1000,y2[i]+1000):
            if coor[x][y] == 0:
                coor[x][y] += 1
                total += 1

for x in range(x1[2]+1000,x2[2]+1000):
    for y in range(y1[2]+1000,y2[2]+1000):
        if coor[x][y] != 0:
            coor[x][y] = 0
            total -= 1


print(total)
