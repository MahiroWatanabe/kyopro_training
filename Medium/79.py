def f(v):
    res = 1
    for i in range(1,v+1):
        res *= i
        res %= MOD
        
    return res

N,M = map(int, input().split())
a,b = 0,0
MOD = 10**9+7

if abs(N-M) >= 2:
    print(0)
elif abs(N-M) == 1:
    ans = f(N)*f(M)
    ans %= MOD
    print(ans)
else:
    ans = f(N)*f(M)
    ans %= MOD
    ans *= 2
    ans %= MOD
    print(ans)