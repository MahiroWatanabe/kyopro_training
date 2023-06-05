N = int(input())
P = list(map(int,input().split()))
cnt = 0
index = 0

while True:
    if index >= N-1:
        break
    
    if P[index]-1 == index:
        cnt += 1
        P[index],P[index+1] = P[index+1],P[index]
        index += 1
    else:
        index += 1
        
if P[-1] == N:
    cnt += 1
print(cnt)