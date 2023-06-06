x, y = map(int, input().split())

ans = float('inf')

x2 = x
y2 = y
if x2 <= y2:
  ans = min(ans, y2 - x2)

x2 = -x
y2 = y

if x2 <= y2:
  ans = min(ans, y2 - x2 + 1)

x2 = x
y2 = -y

if x2 <= y2:
  ans = min(ans, y2 - x2 + 1)

x2 = -x
y2 = -y

if x2 <= y2:
  ans = min(ans, y2 - x2 + 2)

print(ans)