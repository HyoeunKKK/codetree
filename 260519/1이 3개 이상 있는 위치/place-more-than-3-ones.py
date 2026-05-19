n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def one(x,y):
    if grid[x][y] == 1:
        return True
    else:
        return False

total = 0
for i in range(n):
    for j in range(n):
        num = 0
        for d in range(4):
            if in_range(i+dx[d],j+dy[d]) == True:
                if one(i+dx[d],j+dy[d]) == True:
                    num += 1
        if num >= 3:
            total += 1

print(total)