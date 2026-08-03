from collections import deque

grid = [list(map(int,input().split())) for _ in range(4)]
d = str(input())

temp = []
if d == 'L':
    for g in grid:
        l = []
        for i in g:
            if i != 0:
                l.append(i)
        if len(l) == 0:
            l = [0,0,0,0]
            temp.append(l)
        else:
            t = []
            save = 1
            for j in range(len(l)):
                if save == 1:
                    save = l[j]
                else:
                    if l[j] != save:
                        t.append(save)
                        save = l[j]
                    else:
                        t.append(save*2)
                        save = 1
            if save != 1:
                t.append(save)
            for _ in range(4-len(t)):
                t.append(0)
            temp.append(t)
    for t in temp:
        for i in t:
            print(i,end=' ')
        print()

elif d == 'R':
    for g in grid:
        dg = deque()
        cnt = 0
        for i in g[::-1]:
            if i != 0:
                dg.appendleft(i)
        dg = list(dg)
        if len(dg) == 0:
            l = [0,0,0,0]
            temp.append(l)
        else:
            t = deque()
            save = 1
            for j in range(len(dg)-1,-1,-1):
                if save == 1:
                    save = dg[j]
                else:
                    if dg[j] != save:
                        t.appendleft(save)
                        save = dg[j]
                    else:
                        t.appendleft(save*2)
                        save = 1
            if save != 1:
                t.appendleft(save)
            for _ in range(4-len(t)):
                t.appendleft(0)
            temp.append(list(t))
    for t in temp:
        for i in t:
            print(i,end=' ')
        print()

elif d == 'U':
    for i in range(4):
        l = []
        for j in range(4):
            if grid[j][i] != 0:
                l.append(grid[j][i])
        if len(l) == 0:
            temp.append([0,0,0,0])
        else:
            t = []
            save = 1
            for k in range(len(l)):
                if save == 1:
                    save = l[k]
                else:
                    if l[k] != save:
                        t.append(save)
                        save = l[k]
                    else:
                        t.append(save*2)
                        save = 1
            if save != 1:
                t.append(save)
            for _ in range(4-len(t)):
                t.append(0)
            temp.append(t)
    for i in range(4):
        for j in range(4):
            print(temp[j][i],end=' ')
        print()

else:
    for i in range(4):
        l = deque()
        for j in range(4):
            if grid[3-j][i] != 0:
                l.appendleft(grid[3-j][i])
        if len(l) == 0:
            temp.append([0,0,0,0])
        else:
            l = list(l)
            save = 1
            t = deque()
            for j in range(len(l)-1,-1,-1):
                if save == 1:
                    save = l[j]
                else:
                    if save != l[j]:
                        t.appendleft(save)
                        save = l[j]
                    else:
                        t.appendleft(save*2)
                        save = 1
            if save != 1:
                t.appendleft(save)
            for _ in range(4-len(t)):
                t.appendleft(0)
            temp.append(t)
    for i in range(4):
        for j in range(4):
            print(temp[j][i],end=' ')
        print()
