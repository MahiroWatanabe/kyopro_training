S = input().strip()

if len(S) < 26:
    used = [0]*26
    for s in S:
        used[ord(s)-97] = 1
    for i in range(26):
        if used[i] == 0:
            print(S+chr(97+i))
            break
else:
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print("-1")
    else:
        for i in range(24,-1,-1):
            if S[i] < S[i+1]:
                for j in range(25,i,-1):
                    if S[j] > S[i]:
                        t = list(S)
                        t[i], t[j] = t[j], t[i]
                        print(''.join(t[:i+1]))
                        exit()