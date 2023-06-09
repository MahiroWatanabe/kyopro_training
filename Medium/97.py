def do(num):
    return num*(num+1)//2

N = int(input())
L,R = 0,10**9

while R-L > 1:
    mid = (L+R)//2
    if do(mid) <= N:
        L = mid
    else:
        R = mid

fault = (1+R)*R//2-N
result = [n for n in range(1,R+1) if n!= fault]

print(*result)