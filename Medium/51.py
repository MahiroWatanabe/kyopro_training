N = int(input())
X = list(map(int,input().split()))
D = sorted(X)
a,b = D[N//2-1],D[N//2]

for i in range(N):
    if X[i] <= a:
        print(b)
    else:
        print(a)