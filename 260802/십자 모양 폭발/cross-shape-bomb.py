n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
bomb = list(map(int,input().split()))

r = bomb[0]-1
c = bomb[1]-1
cnt = box[r][c]

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def bombing(r,c,cnt):
    x = [0,0,1,-1]
    y = [1,-1,0,0]
    box[r][c] = 0
    for i in range(cnt-1):
        for j in range(4):
            if in_range(r + x[j]*(i+1),c + y[j]*(i+1)) == True:
                box[r + x[j]*(i+1)][c + y[j]*(i+1)] = 0


bombing(r,c,cnt)

temp = []
for i in range(n):
    t = []
    cnt = 0
    for j in range(n):
        if box[n-j-1][i] != 0:
            t.append(box[n-j-1][i])
        else:
            cnt += 1
    for k in range(cnt):
        t.append(0)
    temp.append(t)

for i in range(n):
    for j in range(n):
        print(temp[j][n-i-1],end=' ')
    print()

    
