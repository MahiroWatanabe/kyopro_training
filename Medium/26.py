N = int(input())
A = list(map(int,input().split()))
ans = 0
i = 0

while i < len(A):
    j = i
    while j < N-1 and A[j] <= A[j+1]:
        j += 1
    h = i
    while h < N-1 and A[h] >= A[h+1]:
        h += 1
    i = max(h,j) + 1
    ans += 1

print(ans)