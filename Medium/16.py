N = int(input())
S = [int(input()) for _ in range(N)]
dp = [[False]*(10**4+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(10**4+1):
        if dp[i][j]:
            dp[i+1][j+S[i]] = True
            dp[i+1][j] = True
            
ans = 0
for i in range(10**4+1):
    if i%10 != 0 and dp[-1][i]:
        ans = i

print(ans)

# N = int(input())
# S = sorted([int(input()) for _ in range(N)])
# G = sum(S)
# ans = 0

# if G%10 == 0:
#     for i in S:
#         if (G-i)%10 != 0:
#             ans = max(ans,G-i)
#     print(ans)
# else:
#     print(G)