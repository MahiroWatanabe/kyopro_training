W,H,N = map(int, input().split())
S = W*H
LW,RW = 0,W
LH,RH = 0,H

for _ in range(N):
    x,y,a = map(int, input().split())
    if a == 1:
        LW = max(LW,x)
    elif a == 2:
        RW = min(RW,x)
    elif a == 3:
        LH = max(LH,y)
    else:
        RH = min(RH,y)

if LW < RW and LH < RH:
    print((RW-LW)*(RH-LH))
else:
    print(0)