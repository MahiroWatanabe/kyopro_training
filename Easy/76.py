import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,M = map(int, input().split())
PS = [input().split() for _ in range(M)]
DS = defaultdict(int)
already_input = set()
ans_S = 0
ans_P = 0

for i in range(M):
    p,S = PS[i]
    
    if S == "WA" and p not in already_input:
        DS[p] += 1
        
    if S == "AC" and p not in already_input:
        ans_S += 1
        ans_P += DS[p]
        already_input.add(p)

print(ans_S,ans_P)
