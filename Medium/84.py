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
L = sorted(list(map(int,input().split())))
ans = 0

for b in range(N):
    for a in range(b):
        ab = L[a]+L[b]
        r = bisect_left(L,ab)
        l = b+1
        
        ans += max(0,r-l)

print(ans)

# N = int(input())
# L = list(map(int,input().split()))
# cnt = [0 for _ in range(10**6+1)]
# for i in range(N):
#     cnt[L[i]] += 1
# for i in range(1,2010):
#     cnt[i] += cnt[i-1]
# ans = 0
 
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             mi = max(L[i]-L[j],L[j]-L[i])
#             ma = L[i]+L[j]
            
#             cn = 0
#             if 0 <= ma-1:
#                 cn = cnt[ma-1]
#             cn -= cnt[mi]
            
#             if mi < L[i] < ma:
#                 cn -= 1
#             if mi < L[j] < ma:
#                 cn -= 1
            
#             ans += cn

# ans //= 6
# print(ans)