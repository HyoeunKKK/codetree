'''
1. 이동하기: 
x+dx,y+dy에 # 확인 후
있고, (x,y+1)에 아무것도 없으면 전진(x,y+1). 
앞에 뭐 있으면 방향 반시계(dx=-1,dy=0)로 변경
# 없으면 방향 시계
'''

n = int(input())
x,y = map(int,input().split())
grid = [list(input()) for _ in range(n)]

x -= 1
y -= 1

start_x = x
start_y = y

# 확인 필요한 벽 방향(+:반시계, -:시계)
rx = [1,0,-1,0]
ry = [0,1,0,-1]

# 이동하는 방향(+:반시계,-:시계)
dx = [0,-1,0,1]
dy = [1,0,-1,0]

cnt = 0
i = 0
start_i = i

def in_range(x,y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

def go_around():
    global x,y,i,cnt
    if grid[x+rx[i]][y+ry[i]] == '#':
        if in_range(x+dx[i],y+dy[i]) == True:
            if grid[x+dx[i]][y+dy[i]] == '#':
                # print('반시계 회전',x,y)
                i += 1
                i = i % 4
                if start_i == i and start_x == x and start_y == y:
                    # print('제자리돌기',x,y,i)
                    cnt = -1
                    return False
                else:
                    return True
            else:
                # print('직진',x,y)
                x += dx[i]
                y += dy[i]
                if start_i == i and start_x == x and start_y == y:
                    # print('다시돌아옴',x,y)
                    cnt = -1
                    return False
                else:
                    cnt += 1
                    return True
        else:
            cnt += 1
            # print('out-of-range')
            return False
    else:
        # print('시계 회전',x,y)
        i -= 1
        i = i % 4
        x += dx[i]
        y += dy[i]
        if start_i == i and start_x == x and start_y == y:
            # print('다시돌아옴',x,y)
            cnt = -1
            return False
        else:
            cnt += 1
            return True


while True:
    if go_around() == True:
        pass
    else:
        break

print(cnt)
