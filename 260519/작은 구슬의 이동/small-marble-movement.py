n, t = map(int, input().split())
r, c, d = input().split()   # d = L
r, c = int(r), int(c)       # 1,2

# Please write your code here.

maps = {
    'U': 0,
    'D': 1,
    'R': 2,
    'L': 3
}

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def in_range(x,y):
    return 1 <= x and x < n+1 and 1 <= y and y < n+1

dir = maps[d]       # 3
dir_x = dx[dir]     # -1
dir_y = dy[dir]     # 0
for i in range(t):
    if in_range(r+dir_x,c+dir_y) == True:
        r += dir_x
        c += dir_y
    else:
        dir_x = -dir_x
        dir_y = -dir_y

print(r, c)
