weight=float(input("enter your weight"))
height_cm=float(input("enter your height(cm)"))
height_m=height_cm/100
BMI=weight/(height_m**2)
if BMI<=18.5:
    result="Underweight"
if 24.9<=BMI<18.5:
   result="Normal weight"
if 25<=BMI<29.9: 
   result="Over weight"
if 30<=BMI<34.9:
    result="Obesity"
if 35<=BMI<=39.9:
   result="Extreme Obesity"
print(result)    
