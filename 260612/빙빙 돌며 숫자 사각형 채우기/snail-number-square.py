n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

# 오 -> 아래 -> 왼 -> 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
num = 0
dir = 0
x = 0
y = 0

def direction(dir):
    if dir % 4 == 0:
        return 0
    elif dir % 4 == 1:
        return 1
    elif dir % 4 == 2:
        return 2
    else:
        return 3

def in_range(a,b):
    if 0 <= a < n and 0 <= b < m:
        return True
    else:
        return False

d = direction(dir)

for i in range(n*m):
    num += 1
    arr[x][y] = num
    if in_range(x+dx[d],y+dy[d]) == True and arr[x+dx[d]][y+dy[d]] == 0:
        x += dx[d]
        y += dy[d]
    else:
        dir += 1
        d = direction(dir)
        x += dx[d]
        y += dy[d]

for arr1 in arr:
    for i in arr1:
        print(i,end=' ')
    print()


    