N,A,B,C,D = map(int, input().split())
A,B,C,D = A-1,B-1,C-1,D-1
S = input()

for i in range(B,D):
    if S[i] == "#" and S[i+1] == "#":
        print("No")
        exit()

for i in range(A,C):
    if S[i] == "#" and S[i+1] == "#":
        print("No")
        exit()

if C > D:
    for i in range(B,D+1):
        if S[i-1] == "." and S[i] == "." and S[i+1] == ".":
            print("Yes")
            exit()
    print("No")
    exit()

print("Yes")