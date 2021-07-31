from collections import Counter
from math import floor

# O(n) Time | O(1) Space
# My Solution
# Boyer - Moore Majority Vote algorithm

N = int(input())
n = list(map(int, input().rstrip().split()))
print("Output starts here")
count = 0
c = Counter(n)
for i in c.keys():
  if c.get(i) > floor(N/3):
    print(i,end=' ')
    count+=1
if count==0:
  print("No Majority Elements")
  
