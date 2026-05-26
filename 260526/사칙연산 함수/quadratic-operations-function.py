a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

output = 0
if o == '+':
    output = a + c
elif o == '-':
    output = a - c
elif o == '/':
    output = a // c
elif o == '*':
    output = a * c
else:
    output = 0


if output == 0:
    print(False)
else:
    print(a,o,c,'=',output)