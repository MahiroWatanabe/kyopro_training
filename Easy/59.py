S = input()
if not(S[0] == "A" and S[2:-1].count("C") == 1):
    print("WA")
    exit()

for i in S:
    if "A" == i or "C" == i:
        continue
    if not i.islower():
        print("WA")
        exit()
    

print("AC")