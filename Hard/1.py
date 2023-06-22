S = list(input())
N = len(S)
ans = [0 for _ in range(N)]

for i in range(2):
    cnt = 0
    for j in range(N):
        if S[j] == "R":
            cnt += 1
        else:
            ans[j] += cnt//2
            ans[j-1] += (cnt+1)//2
            cnt = 0
            
    ans = ans[::-1]
    S = S[::-1]
    for i in range(N):
        if S[i] == "L":
            S[i] = "R"
        else:
            S[i] = "L"

print(*ans)