N,M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
ans = 0
AB.sort(key=lambda x:x[0])

for i in range(N):
    diff = M-AB[i][1]
        
    if diff >= 0:
        M -= AB[i][1]
        ans += AB[i][0]*AB[i][1]
    else:
        ans += AB[i][0]*M
        M -= M
        break
    
print(ans)