H,W = map(int, input().split())
A = [list(input()) for _ in range(H)]

for i in range(H):
    flag = True
    for j in range(W):
        if A[i][j] == "#":
            flag = False
            break
    if flag:
        for j in range(W):
            A[i][j] = "T"

for i in range(W):
    flag = True
    for j in range(H):
        if A[j][i] =="#":
            flag = False
            break
    if flag:
        for j in range(H):
            A[j][i] = "T"

for i in A:
    if all([j == "T" for j in i]):
        continue
    for j in i:
        if j == "T":
            continue
        print(j,end="")
    print()

# H,W = map(int, input().split())
# A = [input() for _ in range(H)]
# row = [False]*W
# col = [False]*H

# for i in range(H):
#     for j in range(W):
#         if A[i][j] == "#":
#             row[j] = True
#             col[i] = True

# for i in range(H):
#     if col[i]:
#         for j in range(W):
#             if row[j]:
#                 print(A[i][j],end="")
#         print()