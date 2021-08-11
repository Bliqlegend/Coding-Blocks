# Input code
def unique(s):
  stack = []
  for i in s:
    if i in stack: continue
    else: stack.append(i)

  return stack

s = ["un","iq","ue"]
print(unique(s))