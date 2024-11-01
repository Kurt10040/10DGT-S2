# Fence cost calculator in python
# Author: Kurt Medina
# Date: 30/10/2024
# Version: 1

# Asks a [question] then checks if the input is a usable number
def num_check(question):
    # Error messages
    error_1 = "Please enter a number that is more that 0"
    error_2 = "Please enter a number"

    while True: 
        try:
            response = float(input(question)) # asks question and stores the converts the input into a float

            if response and response > 0:
                return response
            else:
                # If the number is not above 0
                print(error_1)

        except ValueError:
            # If the input is not a number
            print(error_2)

keep_going = ""
while keep_going == "":
    # Get width, length, and cost per meter
    width = num_check("Width: ")
    length = num_check("Length: ")
    cpm = num_check("Cost per meter: ") # cpm = cost per meter

    # Calculate perimeter and total cost
    perimeter = 2 * (width + length)
    cost = perimeter * cpm

    # Outputs values
    print()
    print(f"Perimeter: {perimeter}m")
    print(f"Cost: ${cost}")

    # enables looping
    keep_going = input("press enter to keep going or press any key to quit")
    print()

print("thanks for using the fence cost calculator! :D")