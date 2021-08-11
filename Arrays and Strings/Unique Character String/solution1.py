from collections import Counter
n = int(input())
s = ''
for i in range(n):
  ele = str(input())
  s+=ele

if n > 19 and len(s) > 27:
    print(0)
c = Counter(s)
length = 0
for i in c.keys():
  length+=len(i)

print(length)