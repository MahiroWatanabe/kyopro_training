S = input()
ans = [S[0]]
m = ""

for i in range(1,len(S)):
    m += S[i]
    if ans[-1] != m:
        ans.append(m)
        m = ""
        
print(*ans)
print(len(ans))