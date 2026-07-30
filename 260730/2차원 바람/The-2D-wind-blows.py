n,m,q = map(int,input().split())
conc = [list(map(int,input().split())) for _ in range(n)]
wind = [list(map(int,input().split())) for _ in range(q)]

def in_range(r,c):
    if 0 <= r < n and 0 <= c < m:
        return True
    else:
        False

def clockwise(r1,c1,r2,c2):
    r = r1
    c = c1
    real = conc[r][c]
    conc[r][c] = conc[r+1][c]
    for i in range(c2-c1):
        clock = conc[r][c+1]
        conc[r][c+1] = real
        real = clock
        c += 1
    for i in range(r2-r1):
        clock = conc[r+1][c]
        conc[r+1][c] = real
        real = clock
        r += 1
    for i in range(c2-c1):
        clock = conc[r][c-1]
        conc[r][c-1] = real
        real = clock
        c -= 1
    for i in range(r2-r1):
        clock = conc[r-1][c]
        conc[r-1][c] = real
        real = clock
        r -= 1
    
def meaning(r,c):
    x = [0,0,0,1,-1]
    y = [0,1,-1,0,0]
    count = 0
    total = 0
    for i in range(5):
        if in_range(r+x[i],c+y[i]) == True:
            count += 1
            total += conc[r+x[i]][c+y[i]]
    m = total // count
    conc2[r][c] = m
    # print(total,count,m)

conc2 = [a[:] for a in conc]

for w in wind:
    r1 = w[0]-1
    c1 = w[1]-1
    r2 = w[2]-1
    c2 = w[3]-1
    clockwise(r1,c1,r2,c2)
    conc2 = [a[:] for a in conc]
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            meaning(i,j)
    conc = [a[:] for a in conc2]
    # print(conc2)

for i in range(n):
    for j in range(m):
        print(conc2[i][j], end=' ')
    print()

