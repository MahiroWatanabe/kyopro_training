def price(N):
    return A*N+B*(len(str(N)))

A,B,X = map(int, input().split())

if X < price(1):
    print(0)
    exit()

L,R = 1,20**20

while R-L > 1:
    mid = (L+R)//2
    
    if price(mid) <= X:
        L = mid
    else:
        R = mid

if 10**9 < L:
    L = 10**9

print(L)