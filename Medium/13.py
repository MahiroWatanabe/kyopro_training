N = int(input())
TXY = [list(map(int, input().split())) for _ in range(N)]
time = 0
dx,dy = 0,0

for i in range(N):
    dx,dy = abs(TXY[i][1]-dx),abs(TXY[i][2]-dy)
    time = TXY[i][0]-time
    
    if not ((dx+dy) <= time and time%2 == (dx+dy)%2):
        print("No")
        exit()

print("Yes")