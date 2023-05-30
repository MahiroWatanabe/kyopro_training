N,T = map(int, input().split())
t = list(map(int,input().split()))
time = 0

for i in range(N-1):
    diff = t[i+1]-t[i]
    
    if diff < T:
        time += diff
    else:
        time += T

print(time+T)