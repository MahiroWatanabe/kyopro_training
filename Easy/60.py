N = int(input())
T = list(map(int,input().split()))
S = sum(T)
M = int(input())
for _ in range(M):
    P,X = map(int, input().split())
    P -= 1
    if T[P] < X:
        print(S+(X-T[P]))
    else:
        print(S-(T[P]-X))