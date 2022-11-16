a=float(input("first"))
b=float(input("second"))
c=float(input("third"))
if a<b+c or b<a+c or c<a+b:
    result="It is OK"
if a>b+c or b>a+c or c>a+b:
    result= "not possible"
print (result)   

