H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]
XY = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            flag = False
            for x,y in XY:
                dx,dy = x+i,y+j
                if 0 <= dx < H and 0 <= dy < W:
                    if S[dx][dy] == "#":
                        flag = True
            if not flag:
                print("No")
                exit()

print("Yes")