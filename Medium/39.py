K,A,B = map(int, input().split())

if K < A:
    print(1+K)
    exit()
if A < B and B-A >= 3:
    ans = A
    K -= A-1
    if K%2 == 1:
        K -= 1
        ans += 1
    ans += (B-A)*(K//2)
    print(ans)
else:    
    print(1+K)  