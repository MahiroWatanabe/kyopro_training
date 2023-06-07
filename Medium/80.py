N = int(input())
S = input()
A = [chr(ord('a')+i) for i in range(26)]
D = {i:0 for i in A}
ans = 1

for i in S:
    D[i] += 1

for i,j in D.items():
    if j != 0:
        ans *= j+1
        
ans %= 10**9+7

print(ans-1)