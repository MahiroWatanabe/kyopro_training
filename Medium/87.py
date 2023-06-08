N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
min_value, max_value = 0,0
max_array = []
S = 0

for i in range(N):
    if A[i] < B[i]:
        cnt += 1
        min_value += B[i]-A[i]
    elif A[i] > B[i]:
        max_value += A[i]-B[i]
        max_array.append([i,A[i]-B[i]])
        
max_array.sort(reverse=True, key= lambda x:x[1])

if min_value == 0:
    print(0)
elif min_value <= max_value:
    for i in range(len(max_array)):
        S += max_array[i][1]
        cnt += 1
        if min_value <= S:
            print(cnt)
            exit()
else:
    print(-1)