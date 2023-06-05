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
Q = int(input())
D = deque(list(S))
flag = True

for _ in range(Q):
    T,*_a = input().split()
    if T == "1":
        flag = not flag
    else:
        F,C = _a
        if flag:
            if F == "1":
                D.appendleft(C)
            else:
                D.append(C)
        else:
            if F == "1":
                D.append(C)
            else:
                D.appendleft(C)

print("".join(D) if flag else "".join(D)[::-1])