N = int(input())
T,A = map(int, input().split())
H = list(map(int,input().split()))
ans = 0
current_num = 10**18

for i in range(N):
    num = abs(A-T-H[i]*0.006)
    
    if current_num >= num:
        current_num = num
        ans = i

print(ans+1)