N,M = map(int, input().split())
Judge = [0] * (M+1)
cnt = 0

for _ in range(N):
    K,*_A = map(int, input().split())
    for i in _A:
        Judge[i-1] += 1

for i in Judge:
    if i == N:
        cnt += 1

print(cnt)