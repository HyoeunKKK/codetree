n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False


dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]


def change_num(cnt):
    for i in range(n):
        for j in range(n):
            if cnt == grid[i][j]:
                max_grid = 0
                for k in range(8):
                    x = i+dx[k]
                    y = j+dy[k]
                    if in_range(x,y) == True:
                        if grid[x][y] > max_grid:
                            max_grid = grid[x][y]
                            max_r = x
                            max_c = y
                grid[i][j] = max_grid
                grid[max_r][max_c] = cnt
                return grid

for t in range(m):
    for cnt in range(1,n**2+1):
        grid = change_num(cnt)


for g in grid:
    for i in g:
        print(i,end=' ')
    print()