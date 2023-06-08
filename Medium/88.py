x = int(input())
ans = (x//11)*2
b = x%11

if b == 0:
    print(ans)
elif b <= 6:
    print(ans+1)
else:
    print(ans+2)