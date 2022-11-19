# Data Types

# Strings

print("Hello"[0]) # counting in binary starts with 0.
print("123" + "456") # The computer recognize the characters like text and needs to be declared as integer or a float(with decimals). 
#This will simply concactenate the string.

# Integer (whole numbers without decimal points.)
# Integers are declared by simply typing out the number as showed bellow.
print(123 + 456)

#Large integer numbers are traditionally seperated by commas but in Python you seperate by using underscore.
print(5_333_999 + 4_666_001)

# Float (floating point number)
3.14159

# Boolean
True
False

num_of_char = len(input("What is your name? "))

new_num_of_char = str(num_of_char) 
#the integer stored inside of the new variable is now declared as a string so when printed it will display what we want.
#the reason we have to do it this way is because printing a string and a integer will throw a TypeError and not be printed,
#but using a string and a variable will not.

print("You have " + new_num_of_char + " in your text") 
#   print(type(number_of_char)) #Prints out the type of data 

#This prints out the type of data that is stored inside of a, which is an integer
a = 123
print(type(a)) 

#This converts the integer into a string
a = str(123)
print(type(a))
 
 #This converts the string into a float (number with decimal points)
a = float(123)
print(type(a))

#3 + 5 addition
#7 - 4 subtraction
#3 * 5 multiplication
#6 / 3 division always return as float
#2 ** 2 exponent

#PEMDASLR - ORDER OF PRIORITY
#()
#**
#* / #Left side prioritezed
#+ - #Left side prioritezed 
#print(3 x 3 + 3 / 3 - 3)

print(round(8 / 3, 2))
#      ^rounds a float,^2 =  decimal places
#or you can use floor division = //

# / = floating point type even if no decimal points
# // = integer


# F-String has now converted the data types into text, the curly brackets places our variables with different data types
score = 0 #integer
height = 1.8 #float
isWinning = True #boolean
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")