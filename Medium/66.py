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
AB = [list(map(int, input().split())) for _ in range(N)][::-1]
cnt = 0

for i in range(N):
    AB[i][0] += cnt
    current_cnt = ceil(AB[i][0]/AB[i][1])*AB[i][1]-AB[i][0]
    cnt += current_cnt

print(cnt)