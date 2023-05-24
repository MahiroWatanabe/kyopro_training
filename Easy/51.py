N,A,B = map(int, input().split())
ans = 0

for i in range(1,N+1):
    num = 0
    for j in str(i):
        num += int(j)
    if A <= num <= B:
        ans += i

print(ans)