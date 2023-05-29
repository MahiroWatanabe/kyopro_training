import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
S = input()
ans = 0

for i in range(N):
    a,b = S[:i],S[i:]
    A,B = list(set(list(a))),list(set(list(b)))
    D = defaultdict(int)
    cnt = 0
    
    for j in range(len(A)):
        D[A[j]] += 1
    
    for j in range(len(B)):
        D[B[j]] += 1
    
    for value in D.values():
        if value >= 2:
            cnt += 1
    ans = max(ans,cnt)

print(ans)