n,r,c = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def simulation(r,c):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    start = grid[r][c]
    for i in range(4):
        x = r+dx[i]
        y = c+dy[i]
        if in_range(x,y) == True and grid[x][y] > start:
            temp.append(grid[x][y])
            return x,y
    return -1,-1


r -= 1
c -= 1
temp = [grid[r][c]]

while True:
    if r == -1 and c == -1:
        break
    else:
        r,c = simulation(r,c)

for t in temp:
    print(t,end=' ')