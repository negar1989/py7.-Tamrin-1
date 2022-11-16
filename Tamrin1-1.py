import math
x=float(input("enter x:"))
Radian=(x*math.pi)/180
op=input()
if op=="radical":
    result=(math.sqrt(x))
if op=="sin":
    result=math.sin(Radian)  
if op=="cos":
    result=math.cos(Radian)
if op=="tan":
    result=math.tan(Radian)    
if op=="cot":
    result=math.cot(Radian)
if op=="factorial":
    result=math.factorial(x)
print(result)