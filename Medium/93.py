def do(bit):
    flag = False
    cnt = 0
    for i in range(M):
        flag = False
        cnt2 = 0
                
        for k in range(KS[i][0]):
            if (bit >> KS[i][k+1]-1) & 1:
                cnt2 += 1
        
        if cnt2%2 == P[i]:
            cnt += 1

    if cnt == M:
        flag = True
    
    return flag

N,M = map(int, input().split())
KS = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int,input().split()))
ans = 0

for bit in range(2**N):
    flag = do(bit)
    if flag:
        ans += 1

print(ans)