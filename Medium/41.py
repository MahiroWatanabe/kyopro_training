S = input()
D = set(S)
ans = 10*18

for value in D:
    S_E = S
    cnt = 0
    
    while True:
        temp_2 = ""
        if len(set(S_E)) == 1:
            ans = min(ans,cnt)
            break
            
        for i in range(len(S_E)-1):
            if S_E[i] == value or S_E[i+1] == value:
                temp_2 += value
            else:
                temp_2 += S_E[i]
                
        S_E = temp_2
        cnt += 1            

print(ans)