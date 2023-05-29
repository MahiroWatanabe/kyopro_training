A,B,C = sorted(map(int, input().split()))

# if C%2 == 0:
#     print(0)
# else:
#     a = A*B*(C//2+1)
#     b = A*B*(C//2)
#     print(a-b)
    
if A%2 == 0 or B%2 == 0 or C%2 == 0:
    print(0)
else:
    print(min(A*B,B*C,A*C))