from math import atan2, degrees

A, B, X = map(int, input().split())
X /= A


if X <= A*B/2:
    t = 2*X / B
    ans = atan2(B, t)
    ans = degrees(ans)
else:
    t = 2*(A*B - X) / A
    ans = atan2(t, A)
    ans = degrees(ans)



print(ans)