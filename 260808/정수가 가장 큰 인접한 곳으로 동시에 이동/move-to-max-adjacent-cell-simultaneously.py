n, m, T = map(int, input().split())

# Create n x n grid
grid = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
# r = [pos[0] for pos in marbles]
# c = [pos[1] for pos in marbles]

# Please write your code here.

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for t in range(T):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    m = []
    for r,c in marbles:
        r -= 1
        c -= 1
        max_g = 0
        max_r = 0
        max_c = 0
        for i in range(4):
            if in_range(r+dx[i],c+dy[i]) == True:
                if grid[r+dx[i]][c+dy[i]] > max_g:
                    max_g = grid[r+dx[i]][c+dy[i]]
                    max_r = r+dx[i]
                    max_c = c+dy[i]
        temp[max_r][max_c] += 1
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 1:
                m.append((i+1,j+1))
    marbles = [(r,c) for r,c in m]
    # print(marbles)

print(len(marbles))
    
    
        

