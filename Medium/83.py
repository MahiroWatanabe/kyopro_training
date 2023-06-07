N = int(input())
B = list(map(int,input().split()))
ans = []

for j in range(N):
    for i in range(len(B)-1,-1,-1):
        if i+1 == B[i]:
            ans.append(B[i])
            B = B[:i]+B[i+1:]
            break

if len(ans) == N:
    print(*ans[::-1])
else:
    print(-1)