R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

def color(c):
    if c == 'W':
        return 'B'
    else:
        return 'W'

# def in_range(x,y):
#     if 0 <= x < R and 0 <= y < C:
#         return True
#     else:
#         return False

# def jump(x,y,target):
#     for i in range(R-x-1):
#         x += 1
#         for j in range(C-y-1):
#             y += 1
#             if grid[x][y] == target:
#                 return True
#             else:
#                 continue
    
x = 0
y = 0
num = 0
c = grid[x][y]
c = color(c)
total = 0

hubo = []

if grid[R-1][C-1] == c:
    for i in range(1,R-2):
        for j in range(1,C-2):
            if grid[i][j] == c:
                hubo.append((i,j))
# print(hubo)
    while hubo:
        a,b = hubo.pop()
        c = color(grid[a][b])
        for i in range(a+1,R-1):
            for j in range(b+1,C-1):
                if grid[i][j] == c:
                # print(i,j)
                    num += 1
else:
    num = 0

print(num)