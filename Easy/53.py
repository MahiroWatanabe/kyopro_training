N,M = map(int, input().split())
point = [0 for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    point[a] += 1
    point[b] += 1

print(*point)