n,m,r,c = map(int,input().split())
direction = map(str,input().split())
grid = [list(0 for _ in range(n)) for _ in range(n)]
r -= 1
c -= 1

dice = [1,2,3]          # 윗면,정면,오른쪽면

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def dice_dir(d,r,c,dice):
    if d == 'L':
        if in_range(r,c-1) == True:
            c -= 1
            grid[r][c] = 7-dice[2]
            dice = [dice[2],dice[1],7-dice[0]]
        else:
            return r,c,dice
    elif d == 'R':
        if in_range(r,c+1) == True:
            c += 1
            grid[r][c] = dice[2]
            dice = [7-dice[2],dice[1],dice[0]]
        else:
            return r,c,dice
    elif d == 'U':
        if in_range(r-1,c) == True:
            r -= 1
            grid[r][c] = 7-dice[1]
            dice = [dice[1],7-dice[0],dice[2]]
        else:
            return r,c,dice
    else:
        if in_range(r+1,c) == True:
            r += 1
            grid[r][c] = dice[1]
            dice = [7-dice[1],dice[0],dice[2]]
        else:
            return r,c,dice
    # print(r,c)
    # print(dice)
    # print(grid)
    return r,c,dice


grid[r][c] = 7-dice[0]
# print(r,c)
# print(dice)
# print(grid)
for d in direction:
    r,c,dice = dice_dir(d,r,c,dice)


cnt = 0        
for g in grid:
    for i in g:
        cnt += i

print(cnt)
