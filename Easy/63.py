N = int(input())
a = list(map(int,input().split()))
current_num = 1
cnt = 0

for i in range(N):
    if a[i] == current_num:
        current_num += 1
    else:
        cnt += 1

print(cnt if cnt != N else -1)