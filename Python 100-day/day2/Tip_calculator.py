#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#First i convert the inputs to the appropriate data types.
bill = float(input("Please enter the total amount to pay $ :\n"))
split = int(input("How many people are paying? :\n"))
tip = int(input("How much would you like to tip? 10, 15, 20? :\n"))


tip_percentage = tip / 100
tip_amount = bill * tip_percentage
total_bill = bill + tip_amount
per_pers = total_bill / split

#The results ends in 33.6 even if using the round function so by formatting with the line bellow It will add a 0 regardless.
result = "{:.2f}".format(per_pers)

print(f"the total amount to pay per person is ${result}")