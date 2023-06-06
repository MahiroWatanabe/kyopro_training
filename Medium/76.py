N = int(input())
S = input()
W = []
E = []
cnt_w,cnt_e = 0,0

for i in range(N):
    if S[i] == "W":
        cnt_w += 1
    W.append(cnt_w)
    
S = S[::-1]

for i in range(N):
    if S[i] == "E":
        cnt_e += 1
    E.append(cnt_e)

E = E[::-1]
ans = 10**18

for i in range(N):
    if i == 0:
        ans = min(ans,E[i+1])
    elif i == N-1:
        ans = min(ans,W[i-1])
    else:
        cnt = W[i-1]+E[i+1]
        ans = min(ans,cnt)

print(ans)