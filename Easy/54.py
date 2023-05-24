N = int(input())
D = set()
W = [input() for _ in range(N)]
pre = ""

for i in W:
    if pre == "":
        pre = i
        D.add(i)
        continue
    if i in D or pre[-1] != i[0]:
        print("No")
        exit()
    pre = i
    D.add(i)
        
print("Yes")