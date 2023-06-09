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
V = list(map(int,input().split()))
O_A,K_A = [],[]
ans = 0

if len(set(V)) == 1:
    print(N//2)
    exit()
    
for i in range(N):
    if i%2 == 0:
        K_A.append(V[i])
    else:
        O_A.append(V[i])

K_A = Counter(K_A).most_common()
O_A = Counter(O_A).most_common()
k,o = K_A[0][1],O_A[0][1]

if K_A[0][0] == O_A[0][0]:
    if K_A[1][1] <= O_A[1][1]:
        o = O_A[1][1]
    else:
        k = K_A[1][1]
        
for i,j in K_A:
    ans += j

for i,j in O_A:
    ans += j

print(ans-k-o)