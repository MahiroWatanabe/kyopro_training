N,M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
ans = []

for i in range(N):
    index = 0
    diff = 10**18
    for j in range(M):
        value = abs(AB[i][0]-CD[j][0])+abs(AB[i][1]-CD[j][1])
        if value < diff:
            index = j+1
            diff = value
    ans.append(index)

print(*ans)