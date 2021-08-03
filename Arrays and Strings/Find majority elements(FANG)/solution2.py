# O(n) Time | O(n) Space
# Boyer - Moore Majority Vote algorithm

from math import floor

N = int(input())
n = list(map(int, input().rstrip().split()))

element1 = n[0]
count1 = 1
element2 = 0
count2 = 0

for i in range(N):
    if element1 == n[i % N]:
        count1 += 1
    elif element2 == n[i % N]:
        count2 += 1
    elif count1==0:
        element1 = n[i % N]
        count1 = 1
    elif count2==0:
        element2 = n[i % N]
        count2=1
    else:
        count1-=1
        count2-=1
count1 , count2 = 0,0
for i in range(N):
    if n[i] == element1:
        count1+=1
    elif n[i] == element2:
        count2+=1
if count1 > floor(N/3):
    print(element1,end=' ')
if count2 > floor(N/3):
    print(element2,end=' ')
else:
    print("No Majority Elements")