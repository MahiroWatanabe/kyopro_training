A,B,C = map(int, input().split())
a,b,c = sorted([A,B,C])

if b == a:
    print(c-b)
else:
    cnt = 0
    cnt += (b-a)//2 + (b-a)%2
    c += (b-a)%2
    cnt += c-b
    print(cnt)    