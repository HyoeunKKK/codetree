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
        else:
            d = 'R'
    elif d == 'R':
        if in_range(r,c+1,n) == True:
            c += 1
        else:
            d = 'L'
    elif d == 'U':
        if in_range(r-1,c,n) == True:
            r -= 1
        else:
            d = 'D'
    else:
        if in_range(r+1,c,n) == True:
            r += 1
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
        new_rc, new_d = [],[]
        for i in range(len(rc)):
            r,c = rc[i]
            if new_grid[r][c] == 1:
                new_rc.append([r,c])
                new_d.append(direct[i])
        rc,direct = new_rc,new_d
    print(len(rc))

