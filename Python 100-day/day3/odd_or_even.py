# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

divided = number % 2 #Returns the number divided by 2, until either 0 or 1 is returned.

if divided == 0:
    print("This is an even number.")
else:
    if divided == 1: #Don't need another if indentation, could just use the else as is. I'm learnin.
        print("This is an odd number.")

#if number % 2 == 0: 
# more efficient code compared to adding variable for this.