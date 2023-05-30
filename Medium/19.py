R,G,B,N = map(int, input().split())
cnt = 0

for i in range(N//R+1):
    for j in range(N//G+1):
        current_num = N-(R*i + G*j)
        if current_num%B == 0 and 0 <= current_num//B:
            cnt += 1

print(cnt)