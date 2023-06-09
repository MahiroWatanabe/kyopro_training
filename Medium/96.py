N,M = map(int, input().split())
A = set([int(input()) for _ in range(M)])
dp = [0 for _ in range(N+1)]
dp[0] = 1
MOD = 10**9+7

for i in range(N):
    if i+1 <= N and i+1 not in A:
        dp[i+1] += dp[i]
        dp[i+1] %= MOD
    if i+2 <= N and i+2 not in A:
        dp[i+2] += dp[i]
        dp[i+2] %= MOD

print(dp[-1]%MOD)