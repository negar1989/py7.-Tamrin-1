name=input("enter the name of student")
family=input("enter the family of student")
score1=float(input("enter first score"))
score2=float(input("enter second score"))
score3=float(input("enter third score"))
average=(score1+score2+score3)/3
if average>=17:
    result="Great"
if 12<=average<17:
    result="Normal"
if average<12:
    result="fail"
print(result)    



