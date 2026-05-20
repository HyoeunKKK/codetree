N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

d = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

dx = [1,0,-1,0]
dy = [0,-1,0,1]

x = 0
y = 0
num = 0
ans = -1

for i in range(N):
    dir_num = d[dir[i]]
    dist_num = dist[i]
    for j in range(dist_num):
        x += dx[dir_num]
        y += dy[dir_num]
        num += 1
        if x == 0 and y == 0:
            ans = num
            break
    if x == 0 and y == 0:
        break


print(ans)
    