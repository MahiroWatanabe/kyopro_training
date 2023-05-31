import collections

N,K = map(int,input().split())
A = list(map(int,input().split()))
c = collections.Counter(A)
num = 0
ans = 0

for i in c.most_common():
    num += 1
    if num > K:
        ans += i[1]

print(ans)