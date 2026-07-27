n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt_grid = [list(0 for _ in range(m)) for _ in range(m)]

# Please write your code here.

def find_rect():
    units = []
    for i in range(1,n+1):
        for j in range(1,m+1):                  # 사각형 크기
            # print('rect_size',i,j)
            for cn in range(n-i+1):
                for cm in range(m-j+1):         # 사각형 위치
                    rect = 0
                    # print('rect_start',cn,cm)
                    for sn in range(i):
                        for sm in range(j):
                            # print(sn,sm)
                            rect += grid[cn+sn][cm+sm]
                    start_x = cn
                    start_y = cm
                    end_x = cn+i-1
                    end_y = cm+j-1
                    units.append([start_x,start_y,end_x,end_y,rect])
    units.pop()
    return units

units = find_rect()
del units[-1]
u_num = len(units)

# for i in range(u_num):
#     print(units[i][4], end=',')

def independent(isx,isy,iex,iey,jsx,jsy,jex,jey):
    if iey < jsy:
        return True
    elif isy < jsy < iey:
        if jsx < isx:
            if isx <= jex:
                return False
            else:
                return True
        elif isx <= jsx <= iex:
            return False
        else:
            return True
    else:
        if jsx < isx:
            if jex >= isx and jey >= isy:
                return False
            else:
                return True
        elif isx <= jsx <= iex:
            if jex < isx:
                return True
            else:
                return False
        else:
            return True



grid_total = 0
for i in range(n):
    for j in range(m):
        grid_total += grid[i][j]

best_rects = -5000
for i in range(u_num):
    rect = units[i][4]
    rect_2 = []
    for j in range(u_num):
        if i != j:
            if independent(units[i][0],units[i][1],units[i][2],units[i][3],units[j][0],units[j][1],units[j][2],units[j][3]) == True:
                rect_2.append(units[j][4])
    if len(rect_2) > 0:
        # if grid_total in rect_2:
            # rect_2.remove(grid_total)
        total = rect + max(rect_2)
        # print(rect,max(rect_2),total)
        # print(units[i][0],units[i][1],units[i][2],units[i][3],units[j][0],units[j][1],units[j][2],units[j][3])
        if best_rects < total:
            best_rects = total

print(best_rects)



                    

                    


