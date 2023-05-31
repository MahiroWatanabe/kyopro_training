N = int(input())
S = input()
T = input()

for i in range(N):
    h = i
    j = 0
    while S[h] == T[j]:
        j += 1
        h += 1
        
        if h >= N:
            print(2*N-j)
            exit()

print(2*N)