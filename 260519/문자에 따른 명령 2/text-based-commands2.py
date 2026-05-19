dirs = input()

# Please write your code here.

x = 0
y = 0

Ldx = [0,-1,0,1]
Ldy = [1,0,-1,0]

# Rdx = [0,1,0,-1]
# Rdy = [1,0,-1,0]

def direction(d):
    global n,x,y,dx,dy
    if d == 'L':
        n += 1
        kn = n % 4
        dx = Ldx[kn]
        dy = Ldy[kn]
    elif d == 'R':
        n -= 1
        kn = n % 4
        dx = Ldx[kn]
        dy = Ldy[kn]
    else:
        x += dx
        y += dy
    return x,y

n = 0
dx = 0
dy = 1
for dir in dirs:
    direction(dir)

print(x, y)