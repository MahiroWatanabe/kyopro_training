N,K = map(int, input().split())
ans = 0

for i in range(1,N+1):
    cnt = 0
    current = i
    while True:
        if current >= K:
            break
        current = current*2
        cnt += 1
    temp = 1/N * pow((1/2),cnt)
    ans += temp

print(ans)