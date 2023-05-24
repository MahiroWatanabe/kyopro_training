O = input()
E = input()
ans = ""

for i in range(len(E)):
    ans += O[i]
    ans += E[i]

print(ans+O[-1] if len(O) > len(E) else ans)