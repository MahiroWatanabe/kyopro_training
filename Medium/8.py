N = int(input())
A = list(map(int,input().split()))
line = [1,400,800,1200,1600,2000,2400,2800,5050]
color = set()
cnt = 0

for i in A:
    if 3200 <= i:
        cnt += 1
        continue
    
    for j in range(8):
        if line[j] <= i < line[j+1]:
            color.add(j)

print(max(len(color),1),len(color)+cnt) 