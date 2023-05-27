D,N = map(int, input().split())
if N == 100:
    N += 1
N = str(N)
for i in range(D):
    N += "00"

print(N)