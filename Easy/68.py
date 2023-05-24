N = int(input())
SP = []
for i in range(N):
    S,P = input().split()
    SP.append([S,int(P),i+1])

SP.sort(key = lambda x:(x[0],-x[1]))

for i in range(N):
    print(SP[i][-1])