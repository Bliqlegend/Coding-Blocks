N = int(input())
n = list(map(int, input().rstrip().split()))
currentMax = 0
for i in range(len(n)):
  for j in range(i,len(n)):
    if i!=j:
      area = (j - i) * min(n[i],n[j])
      if area > currentMax:
        currentMax = area
print(currentMax)  
