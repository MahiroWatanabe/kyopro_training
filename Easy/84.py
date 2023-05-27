N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0

for i in range(N):
    farst = min(A[i],B[i])
    cnt += farst
    B[i] -= farst
    secound = min(A[i+1],B[i])
    cnt += secound
    A[i+1] -= secound
    B[i] -= secound

print(cnt)