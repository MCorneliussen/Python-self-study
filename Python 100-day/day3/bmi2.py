# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** int(2) #Can round off on this line instead of adding a variable like below. 
bmi = round(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi} you are underweight. ") #Excellent use of an F-string.
elif bmi < 25:
    print(f"Your BMI is {bmi} you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi} you are obese.")
else:
    print(f"Your BMI is {bmi} you are clinically obese.")


