height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg"))

bmi = weight / (height/100)**2
print("Your BMI is : ", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
     print("You are normal weight.")
elif bmi >= 25 and bmi < 30:
     print("You are overweight")
else:
     print("You are Obese")
