# Making loops in python
# Author: Kurt Medina
# Date: 25/09/2024
# Version: 2
# TODO:
    # Get user input
    # Ask the user for 2 numbers
    # Add the numbers together

# Ask the user for their name
name = input("what is your name?")
print(f"kia ora {name}.")

# Ask the user for two numbers
num_1 = int(input("what is your favorite number?"))
num_2 = int(input("what is your least favorite number?"))

# Add numbers together
sum = num_1 + num_2
print(f"the numbers added together equal to {sum}")


for name_of_loop in range(10):
    print("kimchiii")

keep_going = ""
while keep_going == "":
    print("looping")
    print("still looping")

    keep_going = input("Again? or press any other key to quit")