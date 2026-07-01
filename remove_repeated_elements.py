num = list(map(int, input().split(",")))
newlst = []
for i in num:
    if i in newlst:
        continue
    else:
        newlst.append(i)
print(newlst)

#another approach
num = list(map(int, input().split(",")))
st = set(num)
newlst = list(st)
print(newlst)