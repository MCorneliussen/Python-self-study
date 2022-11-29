# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2 #I concactenate the two names
lower_case = combined_string.lower() #I apply the function .lower() to make all the letters lowercase

t = lower_case.count("t") #I'm now counting how many times the character T is repeated with the function .count()
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e # Not concatenating because the data type returned from the function is integer. I'm now using addition.

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

score = int(str(true) + str(love)) # to properly concactenate the two digits i convert them to strings and then back into integer to be able to check-range them.


if score < 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.") 
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

