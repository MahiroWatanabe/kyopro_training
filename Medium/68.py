import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

H,W = map(int, input().split())
A = [input() for _ in range(H)]
S_cnt = 0

for i in A:
    for j in i:
        if j == "#":
            S_cnt += 1

print("Possible" if S_cnt == H+W-1 else "Impossible")