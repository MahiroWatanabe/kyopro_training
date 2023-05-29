H,W = map(int, input().split())
S = [input() for _ in range(H)]
XY = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

ans = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            for dx,dy in XY:
                x,y = dx+i,dy+j
                if 0 <= x < H and 0 <= y < W:
                    if S[x][y] == "#":
                        ans[i][j] += 1
        else:
            ans[i][j] = "#"

for i in ans:
    for j in i:
        print(j,end="")
    print()