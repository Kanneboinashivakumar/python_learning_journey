import math
a,b,c = map(int, input().split(","))
d = b*b-(4*a*c)
if d>0:
    print("real roots")
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-(d**0.5))/(2*a)
    print(f"{root1,root2}")
elif d==0:
    root=-b/(2*a)
    print("equal roots",root)
else:
    print("imaginary roots")