import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,K = map(int, input().split())
P = list(map(int,input().split()))
D = [0]
ans = 0

for i in range(N):
    s = P[i]*(P[i]+1)/2
    D.append(s/P[i])

D = list(accumulate(D))

for i in range(1,N-K+2):
    temp = D[i+(K-1)]-D[i-1]
    ans = max(ans,temp)

print(ans)