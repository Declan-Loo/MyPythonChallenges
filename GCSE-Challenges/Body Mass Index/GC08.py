"""
GC08	
50	
BODY MASS INDEX	

BMI = weight / height^2 Where weight is taken in kilograms and height in meters. Where weight is taken in kilograms and height in meters.
Underweight - BMI < 18.5
Normal weight - 18.5 <= BMI < 25.0 Overweight - 25.0 <= BMI < 30.0
Obesity - 30.0 <= BMI
Somebody should input weight and height and you calculate the BMI
"""

weight = float(input("Weight: "))
height = float(input("Height: "))
BMI = weight / (height**2)

if BMI < 18.5:
  print("Underweight")
elif BMI >= 18.5 and BMI < 25:
  print("Normal weight")
elif BMI >= 25 and BMI < 30:
  print("Overweight")
else:
  print("Obesity")
