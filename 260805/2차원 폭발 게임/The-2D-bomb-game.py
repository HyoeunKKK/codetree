from collections import deque

n,m,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

'''
1. 열로 묶고
2. 폭탄 터지고
3. 합치기
반복
4. 각 열마다 0 추가해서 다 합치기
5. 오른쪽으로 밀고 90도로 돌리기
'''

def rotate(grid):       # 오른쪽으로 밀고 회전
    rot = []
    for g in grid:
        temp = deque()
        for i in g:
            if i != 0:
                temp.append(i)
            else:
                temp.appendleft(0)
        rot.append(list(temp))
    rot2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rot2[i][j] = rot[n-1-j][i]
    return rot2

def compression(temp):      # 압축: 0 아닌 것끼리
    a_temp = []
    for t in temp:
        if t != 0:
            a_temp.append(t)
    return a_temp

def bombing(temp):                  # 시작 전 압축, temp = 0이면 그대로 리턴, 0아니면 시작: 폭탄 터뜨리고, 압축, 없어질때까지 반복. queue에 넣고 터진 개수만큼 0을 채우고 리턴
    temp = compression(temp)
    if len(temp) == 0:
        temp = [0 for _ in range(n)]
        return temp
    else:
        again = True
        while again:
            again = False
            if len(temp) != 0:
                start = temp[0]
                cnt = 1
                for i in range(1,len(temp)):
                    if start == temp[i]:
                        cnt += 1
                    else:
                        start = temp[i]
                        if cnt >= m:
                            again = True
                            for c in range(cnt):
                                temp[i-c-1] = 0
                        cnt = 1
                if cnt >= m:
                    again = True
                    for c in range(cnt):
                        temp[len(temp)-1-c] = 0
                temp = compression(temp)
        temp = deque(temp)
        for i in range(n-len(temp)):
            temp.appendleft(0)
        return list(temp)
        

def gridding(grid):             # 열로 보면서 bombing 실행 후 grid에 채우고 리턴
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(grid[j][i])
        # print(temp)
        # temp = compression(temp)
        # print(temp)
        # print(temp[0])
        temp = bombing(temp)
        # print(temp)
        for k in range(n):
            grid[k][i] = temp[k]
    return grid



for i in range(k):
    grid = gridding(grid)
    grid = rotate(grid)
grid = gridding(grid)


total = 0
for g in grid:
    for i in g:
        if i != 0:
            total += 1

print(total)
