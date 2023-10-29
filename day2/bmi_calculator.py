# BMI = weight/(height*height)
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = int(weight / height**2)

print("BMI : " + str(bmi))