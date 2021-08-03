from collections import Counter
n = int(input())
s = []
for i in range(n):
  ele = str(input())
  s.append(ele)
c = Counter(s)

length = 0
for i in c.keys():
  length+=len(i)

print(length)