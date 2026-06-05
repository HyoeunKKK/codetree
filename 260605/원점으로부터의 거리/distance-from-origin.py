n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.

class man:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

M = []
for point in points:
    a = point[0]
    b = point[1][0]
    c = point[1][1]
    M.append(man(b,c,a))

M.sort(key = lambda a: abs(a.x)+abs(a.y))

for i in M:
    print(i.num+1)