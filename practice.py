weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = float(input("Enter your age: "))
gender = input("Are you male of female? (eg. m/f)").lower()
BMI = weight / (height/100) ** 2
print("Your BMI is " + str(BMI))
fat = (1.20 * BMI) + (0.23 * age) - 16.2
print(f"Fat percentage in your body is {fat}")
if gender == "f":
    TBW = -2.097 + 0.1069 * height + 0.2466 * weight
    print(f"Your total body water is {TBW}")
if gender == "m":
    TBW1 =  2.447 - 0.09156 * age + 0.1074 * height + 0.3362 * weight
    print(f"Your total body water is {TBW1}")
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")