T = int(input())
N = []
M = []
row_col = []
d = []
for t in range(T):
    n,m = map(int,input().split())
    N.append(n)
    M.append(m)
    rc = []
    direct = []
    for _ in range(m):
        testcase = input().split()
        rc.append([int(testcase[0])-1,int(testcase[1])-1])
        direct.append(str(testcase[2]))
    row_col.append(rc)
    d.append(direct)

def in_range(r,c,n):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def moving(n,new_grid,r,c,d):
    if d == 'L':
        if in_range(r,c-1,n) == True:
            c -= 1
            new_grid[r][c] += 1
        else:
            d = 'R'
            new_grid[r][c] += 1
    elif d == 'R':
        if in_range(r,c+1,n) == True:
            c += 1
            new_grid[r][c] += 1
        else:
            d = 'L'
            new_grid[r][c] += 1
    elif d == 'U':
        if in_range(r-1,c,n) == True:
            r -= 1
            new_grid[r][c] += 1
        else:
            d = 'D'
            new_grid[r][c] += 1
    else:
        if in_range(r+1,c,n) == True:
            r += 1
            new_grid[r][c] += 1
        else:
            d = 'U'
            new_grid[r][c] += 1
    return new_grid,r,c,d


for t in range(T):
    n = N[t]
    m = M[t]
    rc = row_col[t]
    direct = d[t]
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        grid[rc[i][0]][rc[i][1]] = 1
    # print(grid)
    # print(rc,direct)
    for k in range(2*n):
        new_grid = [[0 for _ in range(n)] for _ in range(n)]
        cnt = len(rc)
        if cnt == 0:
            break
        for q in range(cnt):
            r = rc[q][0]
            c = rc[q][1]
            direction = direct[q]
            new_grid,new_r,new_c,new_direction = moving(n,new_grid,r,c,direction)
            rc[q][0] = new_r
            rc[q][1] = new_c
            direct[q] = new_direction
        # print(rc,direct)
        # print(new_grid)
        # print(grid)
        for x in range(n):
            for y in range(n):
                if new_grid[x][y] >= 2:
                    # print('catch')
                    new_grid[x][y] = 0
                    list_del = []
                    for c in range(len(rc)):
                        if rc[c][0] == x and rc[c][1] == y:
                            list_del.append(c)
                    for t in sorted(list_del,reverse=True):
                        del rc[t]
                        del direct[t]
                else:
                    grid[x][y] = new_grid[x][y]
        # print(new_grid)
        # print(grid)
        # print(rc,direct)
    print(len(rc))

