n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# L: 흰색, R: 검은색 2L+2R: 회색


tiles = [list() for _ in range(200000)]

def direction(cur,x,dir):
    if dir == 'R':
        for xi in range(x):
            current = cur + xi
            tiles[current].append('B')
    else:
        for xi in range(x):
            current = cur - xi
            tiles[current].append('W')
    cur = current
    return cur

def tile_color(L):
    if L.count('B') >= 2 and L.count('W') >= 2:
        color = 'G'
    elif len(L) == 0:
        color = 'N'
    else:
        color = L[-1]
    return color

cur = 100000

for i in range(n):
    cur = direction(cur, x[i], dir[i])
    
real = []

for tile in tiles:
    real.append(tile_color(tile))

print(real.count('W'), real.count('B'), real.count('G'))

