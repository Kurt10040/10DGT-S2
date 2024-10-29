# Area and perimeter calculator in python
# Author: Kurt Medina
# Date: 30/10/2024
# Version: 1

def num_check(question):
    error_1 = "Please enter a number that is more that 0"
    error_2 = "Please enter a number"

    while True: 
        try:
            response = float(input(question))

            if response and response > 0:
                return response
            else:
                print(error_1)

        except ValueError:
            print(error_2)

keep_going = ""
while keep_going == "":
    # (assume they put in valid data)
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area & perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Output the area and perimeter
    print()
    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

    keep_going = input("press enter to keep going or press any key to quit")
    print()

print("thanks fior using the are and perimter calculator! :D")