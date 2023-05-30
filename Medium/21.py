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
A = list(map(int,input().split()))
D = Counter(A)
D_A = defaultdict(int)

for key,value in Counter(A).items():
    if value == 1:
        D_A[key] = 0
    else:
        D_A[key] = value*(value-1)//2
        
S = sum(D_A.values())

for i in range(N):
    print(S-(D[A[i]]-1))