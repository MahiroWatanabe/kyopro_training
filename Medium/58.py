N,A,B,C,D = map(int, input().split())
S = input()
dp = [0 for _ in range(N)]
dp[A-1] = dp[B-1] = 1

if C < D:
    for i in range(B-1,N):
        if dp[i]:
            if i+1 < N and S[i+1] == ".":
                dp[i+1] = 1
            if i+2 < N and S[i+2] == ".":
                dp[i+2] = 1
    if dp[D-1]:
        dp = [0 for _ in range(N)]
        dp[A-1] = dp[B-1] = 1
        dp[D-1] = 10
        for i in range(A-1,N):
            if dp[i]:
                if i+1 < N and S[i+1] == "." and dp[i+1] != 10:
                    dp[i+1] = 1
                if i+2 < N and S[i+2] == "." and dp[i+2] != 10:
                    dp[i+2] = 1
        if dp[C-1]:
            print("Yes")
        else:
            print("No") 
else:
    dp[B-1] = 10
    print(dp)
    for i in range(A-1,N):
        if dp[i]:
            if i+1 < N and S[i+1] == "." and dp[i+1] != 10:
                dp[i+1] = 1
            if i+2 < N and S[i+2] == "." and dp[i+2] != 10:
                dp[i+2] = 1
    print(dp)
    if dp[C-1]:
        dp = [0 for _ in range(N)]
        dp[B-1] =  1
        dp[C-1] =10
        for i in range(B-1,N):
            if dp[i]:
                if i+1 < N and S[i+1] == "." and dp[i+1] != 10:
                    dp[i+1] = 1
                if i+2 < N and S[i+2] == "." and dp[i+2] != 10:
                    dp[i+2] = 1
            print(dp)
        if dp[D-1]:
            print("Yes")
        else:
            print("No") 