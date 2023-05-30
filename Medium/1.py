N = int(input())
A = [int(input()) for _ in range(N)]
D = set()
current_index = 0
cnt = 0

while True:
    current_content = A[current_index]
    
    if current_index == 1:
        print(cnt)
        exit()
    
    if current_content in D:
        print(-1)
        exit()
    
    D.add(current_content)
    current_index = current_content-1
    cnt += 1