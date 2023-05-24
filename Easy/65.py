s = input()
A_index = s.index("A")
Z_index = s[::-1].index("Z")
print(len(s)-A_index-1-Z_index+1)
