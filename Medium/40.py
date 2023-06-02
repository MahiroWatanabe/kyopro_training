N,M = map(int, input().split())
X = sorted(list(map(int,input().split())))
D = []

for i in range(M-1):
    D.append(X[i+1]-X[i])
D = sorted(D)[::-1]

print(sum(D[N-1:]))
