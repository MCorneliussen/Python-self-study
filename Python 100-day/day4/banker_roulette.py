# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # use the comma to split the list so that a list of name is returned with index spots
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
list_count = len(names) #I use the len() function to get the total amount of list

random = random.randint(0, list_count) #Made a variable that picks random number from index 0 up to the total amount of people in the list.
person = names[random] #Now i pick a random person out of the list "names".

print(f"{person} is going to buy the meal today!") #Here i display the person who has to pay the bill in an F-string.
