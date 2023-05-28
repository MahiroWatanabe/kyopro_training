def do(bit):
    num = int(ABCD[0])
    value = ABCD[0]
    
    for i in range(3):
        if (bit >> i)&1:
            num += int(ABCD[i+1])
            value += "+" + ABCD[i+1]
        else:
            num -= int(ABCD[i+1])
            value += "-" + ABCD[i+1]
    if num == 7:
        return True,value
    else:
        return False,value   

ABCD = input()

for bit in range(2**3):
    res,value = do(bit)
    if res:
        print(value+"=7")
        exit()