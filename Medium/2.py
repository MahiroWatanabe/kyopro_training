S = input()
D = []
cnt = 0
ans = 0

for i in range(len(S)):
    if S[i] == "B":
        cnt += 1
    D.append(cnt)

for i in range(len(S)):
    if S[i] == "W":
       ans += D[i] 

print(ans)