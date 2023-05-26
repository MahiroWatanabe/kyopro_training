X = int(input())
V = [100,101,102,103,104,105]
dp = [False]*(X+1)
dp[0] = True

for i in range(X+1):
    if dp[i]:
        for j in range(6):
            if i+V[j] <= X:
                dp[i+V[j]] = True

print(1 if dp[-1] else 0)