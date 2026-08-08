n,m,r,c = map(int,input().split())
r -= 1
c -= 1
grid = [list(0 for _ in range(n)) for _ in range(n)]
grid[r][c] = 1

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False


bomb = [(r,c)]
cnt = 1

for i in range(m):
    dist = 2**(i)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    temp = []
    for x,y in bomb:
        for j in range(4):
            if in_range(x+dx[j]*dist,y+dy[j]*dist) == True and grid[x+dx[j]*dist][y+dy[j]*dist] == 0:
                grid[x+(dx[j]*dist)][y+(dy[j]*dist)] = 1
                temp.append((x+dx[j]*dist,y+dy[j]*dist))
                cnt += 1
                # print(x+(dx[j]*dist),y+(dy[j]*dist))
    for a,b in temp:
        if (a,b) not in bomb:
            bomb.append((a,b))

print(cnt)

