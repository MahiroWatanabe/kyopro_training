N = int(input())
A = [0] + list(map(int,input().split())) + [0]
S = 0

for i in range(N+1):
    S += abs(A[i+1]-A[i])

for i in range(1,N+1):
    temp = S
    temp -= abs(A[i]-A[i-1])
    temp -= abs(A[i+1]-A[i])
    temp += abs(A[i+1]-A[i-1])
    print(temp)