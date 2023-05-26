X = int(input())
ans = 1

for i in range(2,1000):
    j = 2
    
    while True:
        num = pow(i,j)
        
        if num <= X:
            ans = max(ans,num)
        else:
            break
        j += 1

print(ans)