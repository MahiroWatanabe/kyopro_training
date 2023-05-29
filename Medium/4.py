S = input()

while True:
    value = S[-1]
    S = S[:-1]
    
    if len(S)%2 == 0:
        a,b = S[:len(S)//2],S[len(S)//2:]
        if a == b:
            print(len(S))
            exit()