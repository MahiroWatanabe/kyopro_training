import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

N,K = map(int, input().split())
A = list(map(int,input().split()))
cnt = 0
MOD = 10**9+7

for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i] > A[j]:
            cnt += 1

ans = cnt*K%MOD
coef = K*(K-1) //2 % MOD
D = Counter(A)
p = 0

for a,c in sorted(D.items()):
    ans = (ans + c*p*coef) % MOD
    p += c

print(ans)