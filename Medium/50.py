L,R = map(int, input().split())
R = min(R,L+2019)
ans = 10**18

for i in range(L,R+1):
    for j in range(L,R+1):
        if i == j:
            continue
        ans = min(ans,i*j%2019)

print(ans)