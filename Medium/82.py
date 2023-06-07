N = int(input())
A = list(map(int,input().split()))
ans = 10**18
L,R = min(A),max(A)

for i in range(L,R+1):
    temp = 0
    for j in range(N):
        temp += (A[j]-i)**2
    ans = min(ans,temp)

print(ans)