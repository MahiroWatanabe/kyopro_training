S = input()
flag = True if S[0] == "0" else False
cnt = 0

for i in range(1,len(S)):
    if flag and S[i] == "0":
        cnt += 1
    
    if not flag and S[i] == "1":
        cnt += 1
    flag = not flag

print(cnt)