S = input()
n,w,s,e = S.count("N"),S.count("W"),S.count("S"),S.count("E")

if (n > 0 and s == 0) or (n == 0 and s > 0):
    print("No")
    exit()

if (w > 0 and e == 0) or (w == 0 and e > 0):
    print("No")
    exit()

print("Yes")