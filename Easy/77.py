N = int(input())
a = sorted(list(map(int,input().split())))[::-1]
ans = 0

for i in range(3*N-N):
    if i%2 == 1:
        ans += a[i]

print(ans)