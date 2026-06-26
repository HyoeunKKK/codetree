n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x_points = []
y_points = []
for x,y in points:
    x_points.append(x)
    y_points.append(y)

max_x = max(x_points)   # 9
max_x_even = max_x//2   # 4
min_x = min(x_points)   # 3
min_x_even = min_x//2   # 1

max_y = max(y_points)   # 7
max_y_even = max_y//2   # 3
min_y = min(y_points)   # 1
min_y_even = min_y//2   # 0

min_total = 100

if max_x_even == min_x_even:
    x = 2
    if max_y_even == min_y_even:
        y = 2
        print(1)
    else:
        for j in range(min_y_even+1,max_y_even+1):
            y = 2*j
            g_1 = 0
            g_2 = 0
            g_3 = 0
            g_4 = 0
            for a,b in points:
                if a < x and b < y:
                    g_1 += 1
                elif a < x and b > y:
                    g_2 += 1
                elif a > x and b > y:
                    g_3 += 1
                else:
                    g_4 += 1
            max_g = max(g_1,g_2,g_3,g_4)
            min_total = min(min_total,max_g)
            
else:
    if max_y_even == min_y_even:
        y = 2
        for i in range(min_x_even+1,max_x_even+1):
            x = 2*i
            g_1 = 0
            g_2 = 0
            g_3 = 0
            g_4 = 0
            for a,b in points:
                if a < x and b < y:
                    g_1 += 1
                elif a < x and b > y:
                    g_2 += 1
                elif a > x and b > y:
                    g_3 += 1
                else:
                    g_4 += 1
            max_g = max(g_1,g_2,g_3,g_4)
            min_total = min(min_total,max_g)
    else:
        for i in range(min_x_even+1,max_x_even+1):
            for j in range(min_y_even+1,max_y_even+1):
                x = 2*i
                y = 2*j
                g_1 = 0
                g_2 = 0
                g_3 = 0
                g_4 = 0
                for a,b in points:
                    if a < x and b < y:
                        g_1 += 1
                    elif a < x and b > y:
                        g_2 += 1
                    elif a > x and b > y:
                        g_3 += 1
                    else:
                        g_4 += 1
                max_g = max(g_1,g_2,g_3,g_4)
                # print(max_g,g_1,g_2,g_3,g_4)
                min_total = min(min_total,max_g)


print(min_total)


