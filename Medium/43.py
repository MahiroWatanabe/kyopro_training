X = int(input())
for i in range(1, X+1):
    tot = i * (i + 1) //2
    if tot >= X:
        print(i)
        break