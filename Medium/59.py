N,A,B,C,D = map(int, input().split())
S = input()

if C < D:
    dp = [-1 for _ in range(N)]
    dp[A-1] = dp[B-1] = 1
    for i in range(B-1,N):
        if dp[i] == 1:
            if i+1 < N and S[i+1] == ".":
                dp[i+1] = 1
            if i+2 < N and S[i+2] == ".":
                dp[i+2] = 1
    if dp[D-1] == 1:
        dp = [-1 for _ in range(N)]
        dp[A-1] = 1
        for i in range(A-1,N):
            if dp[i] == 1:
                if i+1 < N and S[i+1] == "." and dp[i+1] != 0:
                    dp[i+1] = 1
                if i+2 < N and S[i+2] == "." and dp[i+2] != 0:
                    dp[i+2] = 1
        if dp[C-1] == 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    dp = [-1 for _ in range(N)]
    dp[A-1] = 1
    dp[B-1] = 0
    for i in range(A-1,N):
        if dp[i] == 1:
            if i+1 < N and S[i+1] == "." and dp[i+1] != 0:
                dp[i+1] = 1
            if i+2 < N and S[i+2] == "." and dp[i+2] != 0:
                dp[i+2] = 1
    print(dp)
    if dp[C-1] == 1:
        dp = [-1 for _ in range(N)]
        dp[C-1] = 0
        for i in range(B-1,N):
            if dp[i] == 1:
                if i+1 < N and S[i+1] == "." and dp[i+1] != 0:
                    dp[i+1] = 1
                if i+2 < N and S[i+2] == "." and dp[i+2] != 0:
                    dp[i+2] = 1
        if dp[D-1] == 1:
            print("Yes")
        else:
            print("No") 
    else:
        print("No")