A,B = map(int, input().split())
cnt = 0

for i in range(A,B+1):
    current = str(i)
    
    flag = True
    for j in range(len(current)//2):
        if current[j] != current[-(j+1)]:
            flag = False
    if flag:
        cnt += 1
        

print(cnt)