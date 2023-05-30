N,M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]
D = {0:0,1:0,2:0}
judge = set()
ans = ""

for i in range(M):
    if SC[i][0]-1 not in judge:
        D[SC[i][0]-1] = SC[i][1]
        judge.add(D[SC[i][0]-1])
    else:
        print(-1)
        exit()

for i in range(1000):
    current = str(i)
    flag = True
    
    if len(current) == N:
        for j in range(N):
            if current[j] != str(D[j]):
                flag = False
        if flag:
            print(i)
            exit()

print(-1)