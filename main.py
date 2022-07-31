#User input of height and weight.
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#Convert string to float.
height_converted = float(height)
weight_converted = float(weight)

#Calculated BMI.
bmi = weight_converted / (height_converted ** 2)

#BMI output.
print(int(bmi))