N = int(input())
H = list(map(int,input().split()))

for i in range(N-1):
    if not (H[i] <= H[i+1] or H[i] <= H[i+1]-1):
        print("No")
        exit()
    if H[i] != H[i+1]:
        H[i+1] -= 1
        
print("Yes")