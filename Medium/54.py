N,C,K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])
ans = 1
cnt = 1
time = T[0]+K

for i in range(1,N):
    if T[i] <= time and cnt < C:
        cnt += 1
    else:
        cnt = 1
        ans += 1
        time = T[i]+K

print(ans)