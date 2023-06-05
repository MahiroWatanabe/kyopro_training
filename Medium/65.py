import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def lcm(A,B):
    return (A*B)//gcd(A,B)

N,M = map(int, input().split())
S = input()
T = input()
G = gcd(N,M)
L = lcm(N,M)
N,M = N//G,M//G

for i in range(G):
    print(i*N,i*M)
    if S[i*N] != T[i*M]:
        print(-1)
        exit()

print(L)