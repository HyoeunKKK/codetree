n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
how = list(map(int,input().split()))

c_dx = [-1,-1,1,1]
c_dy = [1,-1,-1,1]

dx = [-1,-1,1,1]
dy = [-1,1,1,-1]

def counterclockwise(r,c,x,y):
    order = [x,y,x,y]
    store = box[r][c]
    for i in range(4):
        time = order[i]
        ox = c_dx[i]
        oy = c_dy[i]
        for j in range(time):
            r += ox
            c += oy
            nex = box[r][c]
            box[r][c] = store
            store = nex


def clockwise(r,c,x,y):
    order = [y,x,y,x]
    store = box[r][c]
    for i in range(4):
        time = order[i]
        ox = dx[i]
        oy = dy[i]
        for j in range(time):
            r += ox
            c += oy
            nex = box[r][c]
            box[r][c] = store
            store = nex


r = how[0]-1
c = how[1]-1
x = how[2]
y = how[3]

if how[-1] == 0:
    counterclockwise(r,c,x,y)
else:
    clockwise(r,c,x,y)

for b in box:
    for i in b:
        print(i,end=' ')
    print()