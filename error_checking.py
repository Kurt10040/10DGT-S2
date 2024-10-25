# Error Checking in python
# Author: Kurt Medina
# Date: 25/10/2024
# Version: 3

# region V1
# Code that tests that a valid number is entered
'''done = False # Boolean variable set to false
while not done: # while loop that runs until a valid number is entered
    num = int(input("please enter yuor value:"))
    done = True

    print(f"the number you entered is {num}")'''
# endregion

#r egion V2
# Code that tests that a valid number is enetered (V2)
# Create a function to call every time I ask the user for a number.
# A function is a chick of code that does something.
# I can se a function over and over. To use a function, I 'call' it by writing out its name
'''
def test_int_num(question):
    done = False
    while not done:
        print(question)
        try: # This tries for a valid input
            num = int(input())
            done = True

        except ValueError:
            print(f"That is not a valid number.")
    return(num)

num_1 = test_int_num("please enter  number")
print(f"youve enetered {num_1}!")

num_2 = test_int_num("please enter a second number")
print(f"youve enetered {num_2}!")

num_3 = test_int_num("please enter third number")
print(f"youve enetered {num_3}!")

sum = num_1 + num_2 + num_3
print(f"the sum of {num_1} and {num_2} and {num_3} is {sum}!")
'''
#endregion

# Version 3. Refining my code. Make it more pythonic
# Ask the user to pick a number in a range
def valid_num(question, low, high):
    error = f"Whoops, that is not a number between {low} and {high}!"
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                break
            else:
                print(error+"\n")
        except ValueError:
            print(error)
    return response

num_1 = valid_num("Enter a number between 1 and 15\n", 1, 15)
print(f"You entered {num_1}")

num_2 = valid_num("Now enter a number between 50 and 100\n", 50, 100)
print(f"You entered {num_2}")

num_3 = valid_num("Lastly enter a number between 70 and 80\n", 70, 80)
print(f"You entered {num_3}")

# Multiply the result of num_1, nuym_2, and num_3
multiply = num_1 * num_2 * num_3
print(f"Your three numbers multiplied together are equal to {multiply}")
sum = num_1 + num_2 + num_3
print(f"The total of {num_1}, {num_2}, and {num_3} is {sum}")