S = input()
ans = 0
N = len(S)-1

for i in range(len(S)):
    if S[i] == "U":
        ans += N-i+(2*i)
    else:
        ans += ((N-i)*2)+i

print(ans)