C = [list(map(int, input().split())) for _ in range(3)]
X = [0]*3
Y = [0]*3

for i in range(101):
    for j in range(3):
        Y[j] = C[0][j]-i
    for j in range(3):
        X[j] = C[j][0]-Y[0]
    
    flag = True
    
    for j in range(3):
        for k in range(3):
            if X[j]+Y[k] != C[j][k]:
                flag = False
    
    if flag:
        print("Yes")
        exit()
        
print("No")