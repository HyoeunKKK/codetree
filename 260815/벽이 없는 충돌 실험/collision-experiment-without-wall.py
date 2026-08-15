T = int(input())

direction = {'U':0,'L':1,'R':2,'D':3}

def move_halftime(x,y,d):
    dx = [0,-1,1,0]
    dy = [1,0,0,-1]
    nx = x+dx[d]
    ny = y+dy[d]
    return nx,ny
 
# def duplicate(marbles):
#     new_mb = []
#     marbles_len = len(marbles)
#     visit_list = [0 for _ in range(marbles_len)]
#     for m1 in range(marbles_len):
#         if visit_list[m1] == 0:
#             visit_list[m1] = 1
#             marble_1 = marbles[m1]
#             get_dup_marbles = [marble_1]
#             for m2 in range(marbles_len):
#                 if visit_list[m2] == 0:
#                     marble_2 = marbles[m2]
#                     if marble_1[1] == marble_2[1] and marble_1[2] == marble_2[2]:
#                         visit_list[m2] = 1
#                         get_dup_marbles.append(marble_2)
#             if len(get_dup_marbles) == 1:
#                 if get_dup_marbles[0] not in new_mb:
#                     new_mb.append(get_dup_marbles[0])
#             else:
#                 get_dup_marbles.sort(key=lambda x:(x[3],x[0]))
#                 if get_dup_marbles[-1] not in new_mb:
#                     new_mb.append(get_dup_marbles[-1])
#     return new_mb


def move_all(marbles):
    marb_dict = {}
    for key,value in marbles.items():
        nx,ny = move_halftime(key[0],key[1],value[2])
        if (nx,ny) in marb_dict:
            if value[0] > marb_dict[(nx,ny)][0]:
                marb_dict[(nx,ny)] = value
            elif value[0] == marb_dict[(nx,ny)][0]:
                if value[1] > marb_dict[(nx,ny)][1]:
                    marb_dict[(nx,ny)] = value
        else:
            marb_dict[(nx,ny)] = value
    if len(marbles) != len(marb_dict):
        return marb_dict,True
    else:
        return marb_dict,False


# def time_out(marbles):
#     marb_keys = marbles.keys()
#     marb_keys.
#     marbles.keys().sort(key=lambda x:x[0])
#     x_len = marbles[-1][0] - marbles[0][0]
#     marbles.keys().sort(key=lambda x:x[1])
#     y_len = marbles[-1][1] - marbles[0][1]
#     max_len = x_len + y_len
#     return max_len


for t in range(T):
    n = int(input())
    marbles = {}
    min_x = 2000
    min_y = 2000
    max_x = -2000
    max_y = -2000
    for i in range(n):
        x,y,w,d = input().split()
        marbles[(2*int(x),2*int(y))] = (int(w),i+1,direction[d])
        min_x = min(min_x,int(x))
        min_y = min(min_y,int(y))
        max_x = max(max_x,int(x))
        max_y = max(max_y,int(y))
    max_len = (max_x-min_x) + (max_y-min_y)
    dup_time = -1
    for time in range(max_len):
        marbles,dup = move_all(marbles)
        if dup == True:
            dup_time = time+1
        if len(marbles) <= 1:
            break
    print(dup_time)

