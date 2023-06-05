import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

SA = deque(input())
SB = deque(input())
SC = deque(input())
current_J = 1

while True:
    if current_J == 1:
        if len(SA) == 0:
            print("A")
            exit()
        v = SA.popleft()
        if v == "a":
            current_J = 1
        elif v == "b":
            current_J = 2
        else:
            current_J = 3
    elif current_J == 2:
        if len(SB) == 0:
            print("B")
            exit()
        v = SB.popleft()
        if v == "a":
            current_J = 1
        elif v == "b":
            current_J = 2
        else:
            current_J = 3
    else:
        if len(SC) == 0:
            print("C")
            exit()
        v = SC.popleft()
        if v == "a":
            current_J = 1
        elif v == "b":
            current_J = 2
        else:
            current_J = 3