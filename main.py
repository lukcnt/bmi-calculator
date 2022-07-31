#User input of height and weight.
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#Convert string to float.
height_converted = float(height)
weight_converted = float(weight)

#Calculated BMI.
bmi = weight_converted / (height_converted ** 2)

#BMI interpreted based on the BMI value.
if bmi >= 35:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
elif bmi >= 30:
    print(f"Your BMI is {round(bmi)}, yout are obese.")
elif bmi >= 25:
    print(f"Your BMI is {round(bmi)}, your are slightly overweight.")
elif bmi >= 18.5:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
else:
    print(f"Your BMI is {round(bmi)}, you are underweight.")