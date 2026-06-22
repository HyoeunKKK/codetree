N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.

max_total = 0

for i in range(1,M+1):
    list_s = []
    for k in range(D):
        if m[k] == i:
            if p[k] in sick_p:
                idx = sick_p.index(p[k])
                if t[k] < sick_t[idx]:
                    list_s.append(p[k])
                else:
                    pass
            else:
                list_s.append(p[k])
    # print(list_s)
    list_s = set(list_s)
    for person in sick_p:
        if person in list_s:
            pass
        else:
            list_s = []
    # print(list_s)
    max_total = max(max_total,len(list_s))

print(max_total)