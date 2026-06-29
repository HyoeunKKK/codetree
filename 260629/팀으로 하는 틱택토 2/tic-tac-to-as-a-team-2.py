inp = [input() for _ in range(3)]

# Please write your code here.
A = []
total = []

for i in inp:
    list_a = list(j for j in str(i))
    A.append(list_a)

for list_a in A:
    list_a = list(set(list_a))
    if len(list_a) == 2:
        total.append(list_a)

for i in range(3):
    list_b = []
    for j in range(3):
        list_b.append(A[j][i])
    list_b = list(set(list_b))
    if len(list_b) == 2:
        total.append(list_b)

list_c = []
list_d = []
for i in range(3):
    list_c.append(A[i][i])
    list_d.append(A[i][2-i])
list_c = list(set(list_c))
list_d = list(set(list_d))
if len(list_c) == 2:
    total.append(list_c)
if len(list_d) == 2:
    total.append(list_d)

val = []
for value in total:
    if value not in val:
        val.append(value)

print(len(val))