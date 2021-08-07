L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
D = "789"
lenD, ans = len(D), []
print(D)
if D == "": print('Empty')
def bfs(pos: int, st: str):
    if pos == lenD: ans.append(st)
    else:
        letters = L[D[pos]]
        for letter in letters:
            bfs(pos+1,st+letter)
bfs(0,"")
print("Ans : " ,ans)