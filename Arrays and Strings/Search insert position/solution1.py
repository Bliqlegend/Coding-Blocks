target = 0
found = 0
nums = []
for i in nums:
  if i == target:
    print(nums.index(i))
    found = 1
    break
if found == 0:
    n = min(nums, key=lambda x: (abs(x - target), x))
    if n>target:
      print(nums.index(n))
    else:
      print(nums.index(n)+1)