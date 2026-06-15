n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
'''
패턴 찾기
1. /
위에서 들어오면 왼쪽으로 가기 / 아래에서 들어오면 오른쪽 / 왼쪽에서 들어오면 위 / 오른쪽에서 들어오면 아래
2. \
위에서 들어오면 오른 / 아래에서 들어오면 왼 / 왼쪽에서 들어오면 아래 / 오른쪽에서 들어오면 위
'''

def in_range(x,y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def start_dir(a):
    a -= 1
    row = a // n
    col = a % n
    if row == 0:
        row1 = row
        col1 = col
        d = 'up'
    elif row == 1:
        col1 = n-1
        d = 'right'
        row1 = col
    elif row == 2:
        row1 = n-1
        d = 'down'
        col1 = n-1-col
    else:
        col1 = 0
        d = 'left'
        row1 = n-1-col
    return row1, col1, d        # 0,1,'up'


def direction(char,x,y,indir):
    if char == '/':
        if indir == 'up':
            outdir = 'right'
            y -= 1
        elif indir == 'down':
            outdir = 'left'
            y += 1
        elif indir == 'left':
            outdir = 'down'
            x -= 1
        else:
            outdir = 'up'
            x += 1
    else:
        if indir == 'up':
            outdir = 'left'
            y += 1
        elif indir == 'down':
            outdir = 'right'
            y -= 1
        elif indir == 'left':
            outdir = 'up'
            x += 1
        else:
            outdir = 'down'
            x -= 1
    return x,y,outdir

num = 1
x,y,d = start_dir(k)      # 시작 좌표 및 시작 방향
# print(x,y,d)

while True:
    char = grid[x][y]
    # print(char,d)
    x,y,d = direction(char,x,y,d)
    # print(x,y,d)
    if in_range(x,y) == True:
        num += 1
        continue
    else:
        break

print(num)
