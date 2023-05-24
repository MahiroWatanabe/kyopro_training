A,B,K = map(int, input().split())
ans = set()

for i in range(A,A+K):
    if i > B:
        break
    ans.add(i)

for i in range(B-K+1,B+1):
    if i < A:
        break
    ans.add(i)

print(*sorted(ans))