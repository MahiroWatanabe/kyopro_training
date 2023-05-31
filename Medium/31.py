N = int(input())
A = list(map(int,input().split()))
cnt_Y = 0
cnt_N = 0

for i in A:
    if i%4 == 0:
        cnt_Y += 1
        
    elif i%2 == 0:
        cnt_N += 1

if cnt_N%2 == 0:
    N -= cnt_N
else:
    N -= cnt_N
    N += 1
    
if N//2 <= cnt_Y:
    print("Yes")
else:
    print("No")