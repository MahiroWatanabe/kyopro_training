N,Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]
D = [0]
cnt = 0

for i in range(1,N):
    if S[i-1] == "A" and S[i] == "C":
        cnt += 1
    D.append(cnt)


for i in range(Q):
    l,r = LR[i]
    l,r = l-1,r-1
    print(D[r]-D[l])