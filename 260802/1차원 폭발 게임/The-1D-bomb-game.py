n,m = map(int,input().split())
bomb = list(int(input()) for _ in range(n))

def bombing():
    cnt = 1
    start = bomb[0]
    for i in range(1,len(bomb)):
        if bomb[i] == start:
            cnt += 1
        else:
            start = bomb[i]
            if cnt >= m:
                for j in range(cnt):
                    bomb[i-j-1] = 0
            cnt = 1
    if cnt >= m:
        for j in range(cnt):
            bomb[len(bomb)-1-j] = 0

while True:
    bombing()
    bomb2 = [b for b in bomb]
    temp = []
    for i in bomb:
        if i != 0:
            temp.append(i)
    bomb = temp
    # if bomb == temp:
    #     break
    if len(temp) == 0:
        break
    if bomb2 == bomb:
        break

print(len(bomb))
for i in bomb:
    print(i)


