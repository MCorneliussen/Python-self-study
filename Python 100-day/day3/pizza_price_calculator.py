# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0 

if size == "S":
    bill += 15 
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Error: Try again.")
if add_pepperoni == "Y":
    if "Y":
        if size == "S":
            bill += 2
        elif size == "M":
            bill += 3
        elif size == "L":
            bill += 3

if extra_cheese == "Y":
    if "Y":
        bill += 1

print(f"Your final bill is: ${bill}.") 
