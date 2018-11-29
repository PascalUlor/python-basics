# Display the purpose of the program
print("Welcome to the BMI Calculator")

# Display the instructions to the user
print("Please enter your weight in kilograms and your height in metres")

# Prompt the user to enter their weight
weight = float(input("Please enter your weight: "))

# Prompt the user to enter their height
height = float(input("Please enter your height: "))

# Calculate the BMI of the user
bmi = weight / (height * height)

# Round up the BMI to 1 decimal place
bmi = round(bmi, 1)

# Display the BMI
print("Your BMI is:", bmi)

# Evaluate the BMI and give a verdict
if(bmi<18.5):
    print("Underweight")
elif((bmi>=18.5) and (bmi<25)):
    print("Normal")
elif((bmi>=25) and (bmi<30)):
    print("Overweight")
else:
    print("Obese")
