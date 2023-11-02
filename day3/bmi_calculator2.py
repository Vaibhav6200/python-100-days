# BMI = weight/(height*height)
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = int(weight / height**2)

if bmi < 18.5:
    print(f"you are underweight")
elif bmi < 25:
    print("Normal")
else:
    print("Overweight")