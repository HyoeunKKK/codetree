n = int(input())
block = [int(input()) for _ in range(n)]
ex_1 = list(map(int,input().split()))
ex_2 = list(map(int,input().split()))

temp = []
for i in range(len(block)):
    if ex_1[0]-1 <= i <= ex_1[1]-1:
        pass
    else:
        temp.append(block[i])
block = temp
temp2 = []
for i in range(len(block)):
    if ex_2[0]-1 <= i <= ex_2[1]-1:
        pass
    else:
        temp2.append(block[i])

if len(temp2) == 0:
    print(0)
else:
    print(len(temp2))
    for t in temp2:
        print(t)

