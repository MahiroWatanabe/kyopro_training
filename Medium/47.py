N,P = map(int, input().split())
A = list(map(int,input().split()))
flag = all(i%2 == 0 for i in A)

if flag:
    if P == 0:
        print(pow(2,N))
    else:
        print(0)
else:
    print(pow(2,N-1))