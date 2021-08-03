from collections import Counter

n = 3
s = 'loveleetcode'
c = Counter(s)
num = []
for i in c.keys():
  if c.get(i) == 1:
    b = s.index(i)
    num.append(b)

if not num:
  print(-1)
else:
  print(min(num))
