S = input()
ans = []

for i in S:
    if i == "0":
        ans.append("0")
    elif i == "1":
        ans.append("1")
    else:
        if len(ans) != 0:
            ans.pop()

print("".join(ans))