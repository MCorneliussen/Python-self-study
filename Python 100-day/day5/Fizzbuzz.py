#Thank god for Thonny IDE
result = 0
for numbers in range(1, 101):

    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
        
    elif numbers % 3 == 0:
        print("Fizz")
        
    elif numbers % 5 == 0:
        print("Buzz")
        
    else:
        result = numbers
        print(result)
    