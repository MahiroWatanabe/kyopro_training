from itertools import groupby

S = str(input())
K = int(input())
CHECK = [len(list(g)) for c,g in groupby(S)]
ANSWER = 0
if len(CHECK) == 1:
  ANSWER = len(S) * K // 2
else:
  ANSWER = sum(i//2 for i in CHECK) * K
  if S[0] == S[-1] and CHECK[0]%2 == 1 and CHECK[-1]%2 == 1:
    ANSWER += K-1

print(ANSWER)