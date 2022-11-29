'''# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello Jack Bauer")
    print("how are you")
    print("!")
    
greet()
'''
'''
def greet_with_name(name):
#                     ^ Parameter = name of the data that is being passed in
    print(f"hello {name}")
    print(f"How are you {name}")

greet_with_name("Angela")
#                   ^Argument = the value of the data
'''

#Functions with more than one input.

def greet_with(name, location):
    print(f"Greetings {name}.\nHow is it in {location}? ")
    
greet_with(location="Europe", name="Angela")
