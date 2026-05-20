n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

maps = [[0 for _ in range(n)] for _ in range(n)]

def in_range(a,b):
    if 0 <= a < n and 0 <= b < n:
        return True
    else:
        return False


def safety(a,b):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    safe_num = 0
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if in_range(x,y) == True and maps[x][y] == 1:
            safe_num += 1
    if safe_num == 3:
        print(1)
    else:
        print(0)

for i in points:
    a = i[0]-1
    b = i[1]-1
    maps[a][b] = 1
    safety(a,b)