S = input()
key = "keyence"

for i in range(len(S)):
    for j in range(i,len(S)):
        if key == S[:i]+S[j:]:
            print("YES")
            exit()

print("NO")