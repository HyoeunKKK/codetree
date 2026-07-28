n,m,q = map(int,input().split())
conc = [list(map(int,input().split())) for _ in range(n)]
wind_w = []
wind_h = []
for _ in range(q):
    a,b = input().split()
    wind_w.append(int(a)-1)
    wind_h.append(str(b))

def wind(w,h):
    l = w
    if h == 'L':
        last = conc[l][-1]
        cur = conc[l][0]
        for i in range(m-1):
            c = conc[l][i+1]
            conc[l][i+1] = cur
            cur = c
        conc[l][0] = last
    else:
        first = conc[l][0]
        cur = conc[l][-1]
        for i in range(m-1):
            c = conc[l][m-i-2]
            conc[l][m-i-2] = cur
            cur = c
        conc[l][-1] = first

def direction(h):
    if h == 'L':
        return 'R'
    else:
        return 'L'

def spread_up(w,dir):
    yn = 0
    if w >= 1:
        if acc[w-1] != 1:
            # print('up acc ok')
            for i in range(m):
                # print(conc[w][i],conc[w-1][i])
                if int(conc[w][i]) == int(conc[w-1][i]):
                    # print(1)
                    yn = 1
        else:
            return False
    else:
        return False
    if yn == 1:
        # print('up ok',dir)
        wind(w-1,dir)
        return True
    else:
        # print('up no')
        return False
            
def spread_down(w,dir):
    yn = 0
    if w <= n-2:
        # print('1 accept')
        if acc[w+1] != 1:
            # print('2 accept')
            # print('down acc ok')
            for i in range(m):
                # print(conc[w][i],conc[w+1][i])
                if int(conc[w][i]) == int(conc[w+1][i]):
                    # print(1)
                    yn = 1
        else:
            # print('2 False')
            return False
    else:
        # print('1 False')
        return False
    if yn == 1:
        # print('down ok',dir)
        wind(w+1,dir)
        return True
    else:
        # print('down no')
        return False


for e in range(q):
    acc = [0 for _ in range(n)]
    w = wind_w[e]
    h = wind_h[e]
    wind(w,h)
    acc[w] = 1
    up = True
    down = True
    w1 = w
    w2 = w
    for i in range(n):
        h = direction(h)
        if up == True:
            up = spread_up(w1,h)
            w1 -= 1
            if down == True:
                down = spread_down(w2,h)
                w2 += 1
        else:
            if down == True:
                down = spread_down(w2,h)
                w2 += 1
            else:
                break

for C in conc:
    for c in C:
        print(c,end=' ')
    print()

