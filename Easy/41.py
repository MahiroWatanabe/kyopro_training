N = int(input())
P = list(map(int,input().split()))
current_num = P[0]
cnt = 1

for i in range(1,N):
    if current_num >= P[i]:
        cnt += 1
    current_num = min(current_num,P[i])

print(cnt)