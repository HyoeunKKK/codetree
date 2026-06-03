n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.

words = sorted(word)
for i in words:
    print(i)