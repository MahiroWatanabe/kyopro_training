N = input()

S = sum([int(i) for i in N])
tmp = int(N[0])-1+9*(len(N)-1)

print(max(S,tmp))