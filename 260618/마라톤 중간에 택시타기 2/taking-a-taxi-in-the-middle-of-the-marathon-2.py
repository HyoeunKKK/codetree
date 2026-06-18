n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

def manhattan(x1,y1,x2,y2):
    distance = abs(x1-x2) + abs(y1-y2)
    return distance

min_d = 1000000
total_d = 0
for i in range(n-1):
    total_d += manhattan(x[i],y[i],x[i+1],y[i+1])

for i in range(1,n-1):
    ex = 0
    ex += manhattan(x[i-1],y[i-1],x[i],y[i])
    ex += manhattan(x[i],y[i],x[i+1],y[i+1])
    ex -= manhattan(x[i-1],y[i-1],x[i+1],y[i+1])      
    ex_total = total_d - ex
    min_d = min(min_d,ex_total)

print(min_d)