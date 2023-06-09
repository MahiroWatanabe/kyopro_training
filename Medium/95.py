N,K = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(N)])
current_S = 0

for i in range(N):
    a,b = AB[i]
    current_S += b
    
    if K <= current_S:
        print(a)
        exit()