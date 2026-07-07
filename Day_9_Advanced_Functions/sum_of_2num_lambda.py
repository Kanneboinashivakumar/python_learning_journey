#lambda function
x = int(input("value of x:"))
y = int(input("value of y:"))
sum = lambda x,y:x+y
print(sum(x,y))

#function 
a = int(input("value of a:"))
b = int(input("value of b:"))

def add2num(a,b):
    return a+b
print(add2num(a,b))
