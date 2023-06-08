N,M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]
RXY = [[1,False] for _ in range(N)]
RXY[0][1] = True
ans = 0

for i in range(M):
    x,y = XY[i]
    x,y = x-1,y-1
    
    if RXY[x][1]:
        RXY[y][1] = True
    
    RXY[x][0] -= 1
    RXY[y][0] += 1
    
    if RXY[x][0] == 0:
        RXY[x][1] = False

for i in range(N):
    if RXY[i][1]:
        ans += 1
        
print(ans)