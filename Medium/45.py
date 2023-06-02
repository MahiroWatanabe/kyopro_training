N,M = map(int, input().split())

ans = min(N,M//2)

M -= 2*ans

if M >= 4:
    ans += M//4

print(ans)