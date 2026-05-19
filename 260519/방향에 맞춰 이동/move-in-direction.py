n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x = 0
y = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def direction(d):
    global x
    global y
    if d == 'N':
        x += dx[0]
        y += dy[0]
    elif d == 'S':
        x += dx[1]
        y += dy[1]
    elif d == 'E':
        x += dx[2]
        y += dy[2]
    else:
        x += dx[3]
        y += dy[3]
    return x, y

for i in range(n):
    for j in range(dist[i]):
        direction(dir[i])

print(x, y)