import math
import re

al = "abcdefghijklmnopqrstuvwxyz"
au = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ii():
    return int(input())

def gl():
    return list(map(int, input().split()))

def gs():
    return list(input().split())

def glm(h,w):
    a = []
    for i in range(h):
        a.append(gl())
    return a

def gsm(h,w):
    a = []
    for i in range(h):
        a.append(input())
    return a

def kiriage(n, r):
    if n % r == 0:
        return n // r
    else:
        return (n // r) + 1

def yaku(n):
    ans = []
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
    return ans

def ketawa(n):
    ans = 0
    s = str(n)
    for i in s:
        ans += int(i)
    return ans

vecx = [0, -1, 1, 0]
vecy = [-1, 0, 0, 1]

ans = 10**10
cnt=0
ay="Yes"
an="No"

#main#
n,m=gl()
d={}
for i in range(m):
    s, c = gl()
    if not s in d.keys():
        d[s] = c
    if d[s] != c:
        print(-1)
        exit()
for i in range(1000):
    ok = True
    s = str(i)
    if len(s) != n:
        ok = False
    else:
        for k in d.keys():
            if s[k-1] != str(d[k]):
                ok = False
    if ok:
        print(s)
        exit()
print(-1)
