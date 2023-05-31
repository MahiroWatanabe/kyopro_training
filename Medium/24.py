N,A,B = map(int, input().split())

if A > B:
    print(0)
    exit()

if N == 1:
    if A == B:
        print(1)
        exit()
    else:
        print(0)
        exit()

min_A = (N-1)*A+B
max_B = A+(N-1)*B

print(max_B - min_A+1)