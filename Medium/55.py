import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**7)

def dfs(S,cnt):
    if judge[S] or cnt == 3:
        return
    judge[S] = True
    for to in point[S]:
        if judge[to] == True or to == S:
            continue
        dfs(to,cnt+1)
        
N,M = map(int, input().split())
point = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    point[a].append(b)
    point[b].append(a)

judge = [False for _ in range(N)]

dfs(0,0)

print("POSSIBLE" if judge[-1] else "IMPOSSIBLE")