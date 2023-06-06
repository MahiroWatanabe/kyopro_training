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
S = [input() for _ in range(N)]
D = defaultdict(lambda: 10**18)
for i,j in Counter(S[0]).most_common():
    D[i] = j

for i in range(1,N):
    current_D = defaultdict(lambda: 10**18)
    for i,j in Counter(S[i]).most_common():
        current_D[i] = j
        
    K = []
    
    for i in D:
        if current_D[i] != 10**18:
            D[i] = min(D[i],current_D[i])
        else:
            K.append(i)
    
    for i in K:
        del D[i]

ans = ""
for i,j in D.items():
    ans += i*j
    
print("".join(sorted(ans)))