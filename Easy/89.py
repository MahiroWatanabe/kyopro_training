X,Y = map(int, input().split())

cnt = 1
num = X

while True:
    num = num*2
    if num > Y:
        print(cnt)
        exit()
    cnt += 1
