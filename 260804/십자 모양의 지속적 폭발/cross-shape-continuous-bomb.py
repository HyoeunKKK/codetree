from collections import deque

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
bombs  = list(int(input()) for _ in range(m))

def get_row(c):
    r = -1
    for i in range(n):
        if grid[i][c] != 0:
            r = i
            break
    # print(r,c)
    return r

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def bombing(r,c):
    sr = r
    sc = c
    cnt = grid[r][c]
    grid[r][c] = 0
    x = [0,0,1,-1]
    y = [1,-1,0,0]
    for i in range(4):
        for j in range(cnt-1):
            if in_range(r+x[i],c+y[i]) == True:
                r += x[i]
                c += y[i]
                grid[r][c] = 0
            else:
                continue
        r = sr
        c = sc
    # for i in range(n):
    #     for j in range(n):
    #         print(grid[i][j],end=' ')
    #     print()
    
def arranging(grid):
    g = [list(0 for _ in range(n)) for _ in range(n)]
    for i in range(n):
        temp = []
        zeroth = 0
        for j in range(n-1,-1,-1):
            if grid[j][i] != 0:
                temp.append(grid[j][i])
            else:
                zeroth += 1
        for k in range(zeroth):
            temp.append(0)
        for l in range(len(temp)):
            g[l][i] = temp[n-1-l]
    grid = g
    # for i in range(n):
    #     for j in range(n):
    #         print(grid[i][j],end=' ')
    #     print()
    return grid



for c in bombs:
    c -= 1
    r = get_row(c)
    if r != -1:
        bombing(r,c)
        grid = arranging(grid)


for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()