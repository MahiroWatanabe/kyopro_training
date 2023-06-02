def f(L,R):
    global ans
    if L >= R:
        return
    mi = 10**18
    for i in range(L,R):
        mi = min(mi,H[i])
    
    ans += mi
    
    for i in range(L,R):
        H[i] -= mi
    print(L,R)
    print(H)
    
    D = []
    D.append(-1)
    for i in range(L,R):
        if H[i] == 0:   
            D.append(i)
    D.append(R)
    n = len(D)
    for i in range(n-1):
        f(D[i]+1,D[i+1])

N = int(input())
H = list(map(int,input().split()))
ans = 0
f(0,N)
print(ans)