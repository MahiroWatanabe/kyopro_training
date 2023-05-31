N,Y = map(int, input().split())

for i in range(N+1):
    for j in range(N+1):
        n = N-(i+j)
        if n >= 0 and 1000*i + 5000*j + 10000*n == Y:
            print(n,j,i)
            exit()

print(-1,-1,-1)