import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

S = input()
D = deque()
cnt = 0

for i in range(len(S)):
    D.append(S[i])
    
    if len(D) >= 2:
        b = D.pop()
        a = D.pop()
        if a == b:
            D.append(a)
            D.append(b)
            continue
        cnt += 2

print(cnt)