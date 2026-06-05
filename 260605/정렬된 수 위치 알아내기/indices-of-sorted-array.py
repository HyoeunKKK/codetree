n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

class Seq:
    def __init__(self, num, seq):
        self.num = num
        self.seq = seq

S = []
for i in range(n):
    S.append(Seq(sequence[i],i+1))

S.sort(key = lambda x: (x.num, x.seq))

class Seq2:
    def __init__(self, num, seq, seq2):
        self.num = num
        self.seq = seq
        self.seq2 = seq2

S2 = []
for i in range(n):
    S2.append(Seq2(S[i].num, S[i].seq, i+1))

S2.sort(key = lambda x: x.seq)

for s in S2:
    print(s.seq2, end=' ')