n,m = map(int,input().split())
grid = [list([int(t)] for t in input().split()) for _ in range(n)]
numbers = list(map(int,input().split()))

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def num_to_rc(num):
    for r,sub_list in enumerate(grid):
        for c,sub_sub in enumerate(sub_list):
            for k,value in enumerate(sub_sub):
                if value == num:
                    return int(r),int(c),int(k)

def move(r,c,k,num,grid):
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]
    max_num = 0
    max_nr = 0
    max_nc = 0
    max_j = -1
    for i in range(8):
        nr = r+dr[i]
        nc = c+dc[i]
        if in_range(nr,nc) == True:
            nlen = len(grid[nr][nc])
            if nlen != 0:
                for j in range(nlen):
                    # print(grid[nr][nc][j])
                    # print(type(grid[nr][nc][j]),type(max_num))
                    if grid[nr][nc][j] > max_num:
                        max_num = grid[nr][nc][j]
                        max_nr = nr
                        max_nc = nc
                        max_j = j
    if max_num != 0:
        grid[max_nr][max_nc].extend(grid[r][c][k:])
        grid[r][c] = grid[r][c][:k]
    return grid
        

for num in numbers:
    r,c,k = num_to_rc(num)
    grid = move(r,c,k,num,grid)

for i in range(n):
    for j in range(n):
        if len(grid[i][j]) == 0:
            print(None)
        else:
            for k in range(len(grid[i][j])-1,-1,-1):
                print(grid[i][j][k],end=' ')
            print()