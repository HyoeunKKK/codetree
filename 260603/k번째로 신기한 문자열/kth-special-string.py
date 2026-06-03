n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

list_a = []

t = list(t)
len_t = len(t)

for str_cha in str:
    cha = list(str_cha)
    if t == cha[0:len_t]:
        list_a.append(str_cha)

sorted_cha = sorted(list_a)
print(sorted_cha[k-1])
    